from flask.helpers import get_root_path
from app.models.groups import Groups
from app.models import storage
from app.models.groupMemebers import GroupMembers
from app.models.groupMessages import GroupMessages
from flask import jsonify


def create_group(data):
    name = data.get("name")
    description = data.get("description")
    created_by = data.get("created_by")

    if not name or not created_by:
        return {"error": "Missing required fields"}

    new_group = Groups(name=name, description=description,
                       created_by=created_by)
    new_group.save()
    new_member = GroupMembers(group_id=new_group.id,
                              user_id=created_by, is_admin=True)
    new_member.save()
    print(new_group.to_dict())
    return {"message": "Group created successfully"}


def list_groups(query_params):
    groupsList = []
    if query_params.get("search"):
        groups = storage.search(Groups, query_params["search"])
    else:
        groups = storage.all("Group")
    if groups is None:
        return {"error": "No groups found"}, 404
    for group in groups:
        groupDict = group.to_dict()
        if group.members:
            groupDict["members"] = group.members.to_dict()
        groupsList.append(groupDict)
    return jsonify(groupsList), 200


def get_group_details(group_id):
    group = storage.get(Groups, id=group_id)
    if not group:
        return {"error": "Group not found"}, 404
    return jsonify(group.to_dict())


def join_group(group_id, user_id):
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404
    member = GroupMembers(group_id=group_id, user_id=user_id)
    member.save()
    return {"message": "Successfully joined the group"}


def leave_group(group_id, user_id):
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404
    member = group.memebers.filter_by(user_id=user_id).first()
    if not member:
        return {"error": "Not a group member"}, 400
    storage.delete(member)
    return {"message": "Successfully left the group"}


def add_group_members(data):
    group_id = data.get("group_id")
    user_ids = data.get("user_ids")
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404
    member = GroupMembers(group_id=group_id, user_id=user_ids)
    member.save()
    return {"message": "Members added successfully"}


def send_group_message(group_id, user_id, content):
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404
    message = GroupMessages(
        group_id=group_id, user_id=user_id, content=content)
    message.save()
    return {"message": "Message sent to the group"}


def get_group_messages(group_id):
    messages = storage.get(GroupMessages, id=group_id)
    return jsonify(messages)

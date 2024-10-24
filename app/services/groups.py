from app.models.groups import Groups
from app.models import storage
from app.models.user import Users
from app.models.groupMemebers import GroupMembers
from app.models.groupMessages import GroupMessages
from flask import jsonify
from app.utils.sanitization import sanitize_object


def create_group(data):
    name = data.get("name")
    description = data.get("description")
    created_by = data.get("created_by")

    if not name or not created_by:
        return {"error": "Missing required fields"}

    new_group = Groups(name=name, description=description, created_by=created_by)
    new_group.save()
    new_member = GroupMembers(group_id=new_group.id, user_id=created_by, is_admin=True)
    new_member.save()
    print(new_group.to_dict())
    return {"message": "Group created successfully"}


def list_groups(query_params):
    groupsList = []
    groupDict = {}
    if query_params.get("search"):
        groups = storage.search(Groups, query_params["search"])
    else:
        groups = storage.all(Groups)
        print(groups)
        if groups is None:
            return {"error": "No groups found"}, 404
        for group in groups:
            groupDict = group.to_dict()
            groupDict["members"] = len([member.to_dict() for member in group.members])
            print(groupDict)
            groupsList.append(groupDict)
    return jsonify(groupsList), 200


def my_groups(user_id):
    groupsList = []
    groupDict = {}
    groups = storage.all(Groups)
    if groups is None:
        return {"error": "No groups found"}, 404
    for group in groups:
        groupDict = group.to_dict()
        groupDict["members"] = [member.to_dict() for member in group.members]

        for member in groupDict["members"]:
            groupDict["members"] = len([member.to_dict() for member in group.members])

            if member["user_id"] == user_id:
                groupsList.append(groupDict)
    return jsonify(groupsList), 200


def get_group_members(group_id):
    members = GroupMembers.query.filter_by(group_id=group_id).all()
    if not members:
        return jsonify({"error": "Group not found or no members"}), 404
    return jsonify(
        [{"name": member.user.name, "email": member.user.email} for member in members]
    ), 200


def join_group(group_id, user_id):
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404

    existing_member = storage.all(GroupMembers)
    for member in existing_member:
        if member.group_id == group_id and member.user_id == user_id:
            return {"error": "User is already a member of this group"}, 400
    member = GroupMembers(group_id=group_id, user_id=user_id)
    member.save()
    return {"message": "Successfully joined the group"}


def get_group_details(group_id):
    group = storage.get(Groups, group_id)
    if not group:
        return {"error": "Group not found"}, 404

    group_dict = group.to_dict()

    members = storage.all(GroupMembers)
    for member in members:
        if member.group_id == group_id:
            group_dict["members"] = len([member.to_dict() for member in group.members])

    messages = GroupMessages.query.filter_by(group_id=group_id).all()
    group_dict["messages"] = [
        {
            "user_id": message.user_id,
            "content": message.content,
            "timestamp": message.timestamp,
        }
        for message in messages
    ]

    return jsonify(group_dict), 200


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
    message = GroupMessages(group_id=group_id, user_id=user_id, content=content)
    message.save()
    return {"message": "Message sent to the group"}


def get_group_messages(group_id):
    messages = storage.get(GroupMessages, id=group_id)
    return jsonify(messages)


def get_user_profile(user_id):
    user = storage.get(Users, id=user_id)
    if not user:
        return {"error": "User not found"}, 404
    return jsonify(user.to_dict()), 200


def update_user_profile(data, user_id):
    try:
        user = storage.get(Users, user_id)
        if user:
            storage.update(user, data)
            return jsonify({"success": user.to_dict()}), 202
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

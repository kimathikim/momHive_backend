from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.groups import (
    create_group,
    list_groups,
    get_group_details,
    join_group,
    leave_group,
    send_group_message,
    get_group_messages,
    my_groups,
    get_user_profile,
    update_user_profile,
    add_group_members,
)
from app.routes import group_bp


@group_bp.route("/create", methods=["POST"])
@jwt_required()
def create_new_group():
    data = request.get_json()
    creator_id = get_jwt_identity()
    data["created_by"] = creator_id
    return create_group(data)


#
# @group_bp.route("groups/addmember", methods=["POST"])
# @jwt_required()
# def addmember():
#     data = request.get_json()
#     return add_group_members(data)
#
#
@group_bp.route("/groups", methods=["GET"])
@jwt_required()
def get_all_groups():
    query_params = request.args
    return list_groups(query_params)


@group_bp.route("/mygroups", methods=["GET"])
@jwt_required()
def get_my_groups():
    user_id = get_jwt_identity()
    return my_groups(user_id)


@group_bp.route("/groups/<group_id>", methods=["GET"])
@jwt_required()
def group_details(group_id):
    return get_group_details(group_id)


@group_bp.route("/groups/join/<group_id>", methods=["POST"])
@jwt_required()
def join_specific_group(group_id):
    user_id = get_jwt_identity()
    return join_group(group_id, user_id)


@group_bp.route("/groups/leave/<group_id>", methods=["POST"])
@jwt_required()
def leave_specific_group(group_id):
    user_id = get_jwt_identity()
    return leave_group(group_id, user_id)


@group_bp.route("/groups/<group_id>/message", methods=["POST"])
@jwt_required()
def send_message_to_group(group_id):
    user_id = get_jwt_identity()
    data = request.get_json()
    content = data.get("content")
    if not content:
        return {"error": "Message content is required"}, 400
    return send_group_message(group_id, user_id, content)


@group_bp.route("/groups/<group_id>/messages", methods=["GET"])
@jwt_required()
def fetch_group_messages(group_id):
    return get_group_messages(group_id)


@group_bp.route("/update_profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    return update_user_profile(data, user_id)


@group_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    return get_user_profile(user_id)

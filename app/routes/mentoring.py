from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.mentoring import (
    request_mentorship,
    get_mentorships,
    get_available_mentors,
    get_my_mentees,
    get_profile,
)
from app.routes import mentor_bp


@mentor_bp.route("/request", methods=["POST"])
@jwt_required()
def request_session():
    data = request.get_json()
    mentee_id = get_jwt_identity()  # Assuming mentee is the logged-in user
    data["mentee_id"] = mentee_id

    if "mentor_id" not in data:
        return jsonify({"msg": "Mentor ID is required"}), 400

    return request_mentorship(data)


@mentor_bp.route("/my_sessions", methods=["GET"])
@jwt_required()
def my_sessions():
    user_id = get_jwt_identity()
    return get_mentorships(user_id)


@mentor_bp.route("/mentors", methods=["GET"])
@jwt_required()
def get_mentors():
    user_id = get_jwt_identity()
    mentors = get_available_mentors(user_id)
    return jsonify(mentors), 200


@mentor_bp.route("/mentees", methods=["GET"])
@jwt_required()
def get_mentees():
    user_id = get_jwt_identity()
    mentees = get_my_mentees(user_id)
    return jsonify(mentees), 200


@mentor_bp.route("/profile/<user_id>", methods=["GET"])
@jwt_required()
def view_profile(user_id):

    profile = get_profile(user_id)
    if profile:
        return jsonify(profile), 200
    else:
        return jsonify({"msg": "Profile not found"}), 404

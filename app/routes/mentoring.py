from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.mentoring import request_mentorship, get_mentorships
from app.routes import mentor_bp


@mentor_bp.route("/request", methods=["POST"])
@jwt_required()
def request_session():
    data = request.get_json()
    mentee_id = get_jwt_identity()  # Assuming mentee is the logged-in user
    data["mentee_id"] = mentee_id
    return request_mentorship(data)


@mentor_bp.route("/my_sessions", methods=["GET"])
@jwt_required()
def my_sessions():
    user_id = get_jwt_identity()
    return get_mentorships(user_id)

from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.services.events import create_event, get_events
from app.routes import event_bp


@event_bp.route("/create", methods=["POST"])
@jwt_required()
def create_new_event():
    data = request.get_json()
    return create_event(data)


@event_bp.route("/all", methods=["GET"])
@jwt_required()
def show_events():
    return get_events()

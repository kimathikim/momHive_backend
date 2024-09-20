from app.models.event_attendees import EventAttendees
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.events import Events
from app.models import storage
from app.routes import events_bp
from app.services.rate_limiter import rate_limit


# Get all events
@events_bp.route("/events", methods=["GET"])
@jwt_required()
def get_all_events():
    """Retrieve all events."""
    events = storage.all(Events)
    event_list = [event.to_dict() for event in events]
    return jsonify(event_list), 200


@events_bp.route("/events/<event_id>", methods=["GET"])
@jwt_required()
def get_event(event_id):
    """Retrieve a specific event by ID."""
    event = storage.get(Events, event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    return jsonify(event.to_dict()), 200


@events_bp.route("/events", methods=["POST"])
@jwt_required()
def create_event():
    """Create a new event."""
    data = request.json
    required_fields = ["name", "date"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # Create and save the new event
        event = Events(
            name=data["name"],
            description=data.get("description", ""),
            date=data["date"],
            location=data.get("location", ""),
        )
        event.save()
        return jsonify(
            {"message": "Event created successfully", "event": event.to_dict()}
        ), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@events_bp.route("/events/<event_id>", methods=["PUT"])
@jwt_required()
def update_event(event_id):
    """Update an event by ID."""
    event = storage.get(Events, event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.json
    if not data:
        return jsonify({"error": "Missing fields to update"}), 400
    try:
        event.name = data.get("name", event.name)
        event.description = data.get("description", event.description)
        event.date = data.get("date", event.date)
        event.location = data.get("location", event.location)
        event.save()

        return jsonify(
            {"message": "Event updated successfully", "event": event.to_dict()}
        ), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@events_bp.route("/events/<event_id>", methods=["DELETE"])
@jwt_required()
def delete_event(event_id):
    """Delete an event by ID."""
    event = storage.get(Events, event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    try:
        event.delete()
        return jsonify({"message": "Event deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@events_bp.route("/events/<event_id>/attend", methods=["POST"])
@jwt_required()
def attend_event(event_id):
    """Mark the user as attending the event."""
    user_id = get_jwt_identity()

    event = storage.get(Events, event_id)
    if not event:
        return jsonify({"error": "Event not found"}), 404

    attendies = storage.get(EventAttendees, event_id)
    attendee = None
    if not attendies:
        return jsonify({"error": "Event attendees not found"}), 404
    for att in attendies:
        if att.user_id == user_id:
            attendee = att
            break
    if attendee:
        return jsonify({"message": "User is already attending this event"}), 200

    try:
        attendance = EventAttendees(user_id=user_id, event_id=event_id)
        attendance.save()

        return jsonify({"message": "User is now attending the event"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

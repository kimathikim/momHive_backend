from app.models.events import Events
from flask import jsonify
from app.models import storage


def create_event(data):
    name = data.get("name")
    description = data.get("description")
    date = data.get("date")

    if not name or not date:
        return {"error": "Missing required fields"}

    new_event = Events(name=name, description=description, date=date)
    new_event.save()

    return {"message": "Event created successfully"}


def get_events():
    events = storage.all("Events")
    return jsonify(events)


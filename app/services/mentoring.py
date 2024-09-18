from app.models.mentorship import Mentorship
from flask import jsonify
from app.models import storage
from datetime import datetime


def request_mentorship(data):
    mentor_id = data.get("mentor_id")
    mentee_id = data.get("mentee_id")
    topic = data.get("topic")
    status = data.get("status", "pending")
    start_date = data.get("start_date", datetime.utcnow())
    end_date = data.get("end_date")

    if not mentor_id or not mentee_id or not topic:
        return {"error": "Missing required fields"}

    mentorship_request = Mentorship(
        mentor_id=mentor_id,
        mentee_id=mentee_id,
        topic=topic,
        status=status,
        start_date=start_date,
        end_date=end_date,
    )
    mentorship_request.save()

    return {"message": "Mentorship request sent successfully"}


def get_mentorships(user_id):
    mentorships = storage.get(Mentorship, id=user_id)
    return jsonify(mentorships)

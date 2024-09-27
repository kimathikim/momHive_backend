# app/services/mentoring.py

from app.models.mentorship import Mentorship
from app.models.user import Users
from app.models import storage


def request_mentorship(data):
    """
    Request a mentorship session by a mentee with a mentor.
    """
    mentee_id = data.get("mentee_id")
    mentor_id = data.get("mentor_id")
    mentor = storage.get(Users, mentor_id)
    mentee = storage.get(Users, mentee_id)
    if not mentee:
        return {"msg": "Mentee not found"}, 404
    if not mentee or not mentor:
        return {"msg": "Invalid mentor or mentee."}, 400
    if mentee.is_mentor or mentee.is_mentee is False:
        return {"msg": "Invalid mentee or mentor"}, 400
    new_mentorship = Mentorship(mentee_id=mentee_id, mentor_id=mentor_id)
    new_mentorship.save()
    return {"msg": "Mentorship request successful"}, 201


def get_mentorships(user_id):
    """
    Get all mentorship sessions for a user (both as mentor and mentee).
    """
    user = storage.get(Users, user_id)
    if not user:
        return {"msg": "User not found"}, 404

    # Fetch sessions where the user is a mentor
    sessions = storage.all(Mentorship)
    mentor_sessions = [session for session in sessions if session.mentor_id == user_id]
    mentee_sessions = [session for session in sessions if session.mentee_id == user_id]
    # Prepare response
    return {
        "mentor_sessions": [
            {"mentee_id": session.mentee_id, "session_date": session.session_date}
            for session in mentor_sessions
        ],
        "mentee_sessions": [
            {"mentor_id": session.mentor_id, "session_date": session.session_date}
            for session in mentee_sessions
        ],
    }, 200


def get_available_mentors(user_id):
    """
    Fetch all available mentors (excluding the current user).
    """
    users = storage.all(Users)
    mentors = [mentor for mentor in users if mentor.is_mentor is True]

    return [
        {
            "id": mentor.id,
            "name": f"{mentor.first_name} {mentor.second_name}",
            "expertise": mentor.expertise,
        }
        for mentor in mentors
    ]


def get_my_mentees(mentor_id):
    """
    Fetch all mentees assigned to the logged-in mentor.
    """
    users = storage.all(Users)
    mentees = [mentee for mentee in users if mentee.is_mentee is True]

    return [
        {
            "id": mentee.id,
            "name": f"{mentee.first_name} {mentee.second_name}",
            "help_needed": mentee.help_needed,
        }
        for mentee in mentees
    ]


def get_profile(user_id):
    """
    Get detailed profile information for a mentor or mentee.
    """
    user = storage.get(Users, user_id)

    if not user:
        return None

    return {
        "id": user.id,
        "first_name": user.first_name,
        "second_name": user.second_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "expertise": user.expertise if user.is_mentor else None,
        "help_needed": user.help_needed if user.is_mentee else None,
    }

from sqlalchemy import Column, String, ForeignKey
from app.models.base_model import Base, BaseClass


class EventAttendees(Base, BaseClass):
    __tablename__ = "event_attendees"

    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    event_id = Column(String(60), ForeignKey("events.id"), nullable=False)

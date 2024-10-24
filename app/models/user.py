from sqlalchemy import Column, String, Boolean, Text
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class Users(Base, BaseClass):
    __tablename__ = "users"

    first_name = Column(String(128), nullable=False)
    second_name = Column(String(128), nullable=False)
    bio = Column(Text, nullable=True)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    is_mentor = Column(Boolean, default=False)
    expertise = Column(Text, nullable=True)
    is_mentee = Column(Boolean, default=False)
    help_needed = Column(Text, nullable=True)
    mentor_sessions = relationship(
        "Mentorship",
        back_populates="mentor",
        lazy=True,
        foreign_keys="Mentorship.mentor_id",
    )
    mentee_sessions = relationship(
        "Mentorship",
        back_populates="mentee",
        lazy=True,
        foreign_keys="Mentorship.mentee_id",
    )

    sent_messages = relationship("Messages", foreign_keys="Messages.sender_id")
    received_messages = relationship("Messages", foreign_keys="Messages.recipient_id")

    def __init__(self, **kwargs):
        """Initialize the class with relevant details."""
        super().__init__(**kwargs)

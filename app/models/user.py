from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass
from datetime import datetime


class Users(Base, BaseClass):
    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    second_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone_number = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)

    mentorships = relationship(
        "Mentorship",
        back_populates="user",
        lazy=True,
        foreign_keys="mentorship.c.mentor_id",
    )

    mentorships = relationship(
        "Mentorship",
        back_populates="mentee",
        lazy=True,
        foreign_keys="mentorship.c.mentee_id",
    )
    # groups = relationship("GroupMembers", backref="user", lazy=True)
    sent_messages = relationship("Messages", foreign_keys="Messages.sender_id")
    received_messages = relationship(
        "Messages", foreign_keys="Messages.recipient_id")

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

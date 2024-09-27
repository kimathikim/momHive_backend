from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass
from datetime import datetime


class Mentorship(Base, BaseClass):
    __tablename__ = "mentorship"
    mentor_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    mentee_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    # pending, active, completed, etc.
    status = Column(String(128), default="pending")
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    mentor = relationship(
        "Users", back_populates="mentor_sessions", foreign_keys=mentor_id
    )
    mentee = relationship(
        "Users", back_populates="mentee_sessions", foreign_keys=mentee_id
    )

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

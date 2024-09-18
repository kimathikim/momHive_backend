from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass
from datetime import datetime


class MenteeSessions(Base, BaseClass):
    __tablename__ = "menteesessions"
    mentor_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    mentee_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    session_type = Column(String(128), nullable=False)  # 'message' or 'zoom'
    scheduled_time = Column(DateTime, nullable=True)  # for zoom calls
    message_thread_id = Column(
        String(60), ForeignKey("messages.id"), nullable=True
    )  # if it's via messages

    # Relationships
    mentor = relationship("Users", foreign_keys=[mentor_id])
    mentee = relationship("Users", foreign_keys=[mentee_id])
    message_thread = relationship("Messages", foreign_keys=[message_thread_id])

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

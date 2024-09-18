from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base, BaseClass


class Messages(Base, BaseClass):
    __tablename__ = "messages"
    sender_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    recipient_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    content = Column(String(1024), nullable=False)
    conversation_id = Column(String(60), ForeignKey(
        "conversations.id"), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    read = Column(Boolean, default=False)
    sender = relationship(
        "Users", back_populates="sent_messages", foreign_keys=[sender_id]
    )
    recipient = relationship(
        "Users", back_populates="received_messages", foreign_keys=[recipient_id]
    )

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

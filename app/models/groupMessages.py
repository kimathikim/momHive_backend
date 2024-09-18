from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass
from datetime import datetime


class GroupMessages(Base, BaseClass):
    __tablename__ = "group_messages"
    sender_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    group_id = Column(String(60), ForeignKey("groups.id"), nullable=False)
    content = Column(String(1024), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationships
    # sender = relationship(
    #     "Users", back_populates="sent_group_messages", foreign_keys=[sender_id]
    # )

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

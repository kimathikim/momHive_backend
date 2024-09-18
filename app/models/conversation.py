from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class Conversations(Base, BaseClass):
    __tablename__ = "conversations"
    sender = Column(String(60), ForeignKey("users.id"), nullable=False)
    receiver = Column(String(60), ForeignKey("users.id"), nullable=False)

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

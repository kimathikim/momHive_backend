from sqlalchemy import Column, ForeignKey, Boolean, DateTime, String
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass
from datetime import datetime


class Groups(Base, BaseClass):
    __tablename__ = "groups"
    name = Column(String(60), nullable=False)
    description = Column(String(257), nullable=True)
    created_by = Column(String(60), ForeignKey("users.id"), nullable=False)

    members = relationship("GroupMembers", backref="group", lazy=True)
    group_messages = relationship("GroupMessages", backref="groups", lazy=True)

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

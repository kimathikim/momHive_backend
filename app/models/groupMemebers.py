from datetime import datetime

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base_model import Base, BaseClass


class GroupMembers(Base, BaseClass):
    __tablename__ = "groupmembers"
    group_id = Column(String(60), ForeignKey("groups.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    is_admin = Column(String(60), nullable=False, default=False)

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

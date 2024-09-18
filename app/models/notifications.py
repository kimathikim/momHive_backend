from sqlalchemy import Column, String, ForeignKey
from app.models.base_model import Base, BaseClass


class Notifications(Base, BaseClass):
    __tablename__ = "Notifications"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    content = Column(String(1024), nullable=False)

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

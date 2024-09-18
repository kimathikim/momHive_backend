from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from app.models.base_model import Base, BaseClass


class Events(Base, BaseClass):
    __tablename__ = "events"
    name = Column(String(128), nullable=False)
    description = Column(String(256), nullable=True)
    date = Column(DateTime, nullable=False)
    location = Column(String(128), nullable=True)

    def __init__(self, **kwargs):
        """initialize the class with relevant details."""
        super().__init__(**kwargs)

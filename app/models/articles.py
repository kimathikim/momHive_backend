from sqlalchemy import Column, String, Boolean, DateTime, Text
from app.models.base_model import Base, BaseClass


class Article(Base, BaseClass):
    __tablename__ = "articles"

    title = Column(String(256), nullable=False)
    author = Column(String(128), nullable=True)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=False)
    published_at = Column(DateTime, nullable=True)
    source = Column(String(128), nullable=True)
    url = Column(String(256), nullable=True)
    url_to_image = Column(String(256), nullable=True)
    is_featured = Column(Boolean, default=True)
    topic = Column(String(128), nullable=False)

    def __init__(self, **kwargs):
        """Initialize the Article with relevant details."""
        super().__init__(**kwargs)

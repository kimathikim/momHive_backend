#!/usr/bin/env python3
"""DBStorage class for the Hospital prescription management system"""

import os
from sqlalchemy.orm import sessionmaker
from app.models.messages import Messages
from app.models.mentorship import Mentorship
from app.models.mentoringSession import MenteeSessions
from app.models.user import Users
from app.models.groupMemebers import GroupMembers
from app.models.conversation import Conversations
from app.models.groups import Groups
from app.models.articles import Article
from app.models.events import Events
from app.models.event_attendees import EventAttendees
from app.models.groupMessages import GroupMessages
import pymysql


class DBStorage:
    """DBStorage class for the Hospital prescription management system"""

    def __init__(self):
        """Initializes the DBStorage instance"""
        from sqlalchemy import create_engine
        from app.models.base_model import Base

        self.__engine = create_engine(
            "mysql+pymysql://{}:{}@{}/{}".format(
                os.getenv("MH_MYSQL_USER"),
                os.getenv("MH_MYSQL_PWD"),
                os.getenv("MH_MYSQL_HOST"),
                os.getenv("MH_MYSQL_DB"),
            ),
            pool_pre_ping=True,
        )
        if os.getenv("MH_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all
        objects of the given class"""
        classes = [
            Users,
            Conversations,
            Messages,
            EventAttendees,
            GroupMembers,
            GroupMessages,
            Groups,
            Article,
            Mentorship,
            MenteeSessions,
            Events,
        ]
        objects = []
        if cls:
            if cls in classes:
                for obj in self.__session.query(cls).all():
                    objects.append((obj))
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    objects.append((obj))
        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and
        the current database session"""
        from sqlalchemy.orm import scoped_session
        from app.models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session"""
        self.__session.close()

    def get(self, cls, id):
        """get an object from the database"""
        if cls is not None and id is not None:
            obj = self.__session.query(cls).get(id)
            return obj
        return None

    def update(self, obj, data):
        if obj is None or data is None:
            return None
        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        self.save()
        return obj

    def get_by_email(self, cls, email):
        """get an object from the database"""
        if cls is not None and email is not None:
            obj = self.__session.query(cls).filter_by(email=email).first()
            return obj
        return None

    def get_by_code(self, cls, code):
        """get an object from the database"""
        if cls is not None and code is not None:
            obj = self.__session.query(cls).filter_by(otp_code=code).first()
            return obj
        return None

    def get_patient_code(self, cls, code):
        """get an object from the database"""
        if cls is not None and code is not None:
            obj = self.__session.query(cls).filter_by(
                patient_code=code).first()
            return obj
        return None

    def search(self, cls, search_term):
        """Search for a term in all columns of the given class"""
        if cls is not None and search_term is not None:
            from sqlalchemy import or_

            columns = [column for column in cls.__table__.columns]
            query = self.__session.query(cls)
            query = query.filter(
                or_(*[column.ilike(f"%{search_term}%") for column in columns])
            )
            return query.all()
        return None

    def get_messages(self, sender_id, receiver_id):
        from app.models.messages import Messages
        from sqlalchemy import or_, and_

        messages = (
            self.__session.query(Messages)
            .filter(
                or_(
                    and_(
                        Messages.sender_id == sender_id,
                        Messages.receiver_id == receiver_id,
                    ),
                    and_(
                        Messages.sender_id == receiver_id,
                        Messages.receiver_id == sender_id,
                    ),
                )
            )
            .order_by(Messages.timestamp.asc())
            .all()
        )

        return messages

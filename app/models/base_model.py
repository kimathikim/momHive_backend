#!/usr/bin/env python3
"""BaseModel class for the Hospital prescription management system"""

from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from app.utils.date_time import format_datetime, parse_datetime

Base = declarative_base()


class BaseClass:
    """this will be inherited by all model classes in the project"""

    id = Column(
        String(60),
        primary_key=True,
        default=lambda: str(uuid4()),
        unique=True,
        nullable=False,
    )
    created_at = Column(String(60), nullable=False, default=datetime.now())
    updated_at = Column(String(60), nullable=False, default=datetime.now())

    def __init__(self, **kwargs):
        """initializes the base model class"""
        self.id = str(uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

            if kwargs.get(
                "created_at\
            ",
                None,
            ) and isinstance(kwargs["created_at"], str):
                self.created_at = parse_datetime(kwargs["created_at"])
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and isinstance(
                kwargs[
                    "\
            updated_at"
                ],
                str,
            ):
                self.updated_at = parse_datetime(kwargs["updated_at"])
            else:
                self.updated_at = datetime.utcnow()

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        def __str__(self):
            """returns a string representation of the instance"""
            return "{}.{}".format(type(self).__name__, self.id)

    def to_dict(self):
        """returns a dictionary representation of the instance"""
        newDict = self.__dict__.copy()
        newDict.pop("_sa_instance_state", None)
        newDict["created_at"] = format_datetime(self.created_at)
        if "created_at" in newDict:
            newDict["created_at"] = format_datetime(newDict["created_at"])
        if "updated_at" in newDict:
            newDict["updated_at"] = format_datetime(newDict["updated_at"])
        newDict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in newDict:
            del newDict["_sa_instance_state"]
        return newDict

    def save(self):
        self.updated_at = datetime.utcnow()
        from app.models import storage

        storage.new(self)
        storage.save()

    def delete(self):
        from app.models import storage

        storage.delete(self)
        storage.save()

#!/usr/bin/python3
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel():
    """ Base Class all other class will inheret from"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get('id', None) is None:
                self.id = str(uuid4())
            if kwargs.get('created_at', None) is None:
                self.created_at = datetime.now()
            if kwargs.get('updated_at', None) is None:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) [{}]".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )
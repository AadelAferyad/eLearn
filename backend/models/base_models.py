#!/usr/bin/python3
"""
    this is the base model all the other classes will inhert from,
    All the repeated function and variable are here
"""
import models

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base

from uuid import uuid4
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
                # if key == 'birthday':
                #     setattr(self, key, value.strftime('$'))
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get('id', None) is None:
                self.id = str(uuid4())
            if kwargs.get('created_at', None) is None:
                self.created_at = datetime.utcnow()
            if kwargs.get('updated_at', None) is None:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def __str__(self):
        return "[{}] ({}) [{}]".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)
        models.storage.save()

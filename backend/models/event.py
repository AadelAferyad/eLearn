#!/usr/bin/python3
from models.base_models import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Event(BaseModel, Base):
    """
        event class
    """

    __tablename__ = 'events'
    name = Column(String(60), nullable=False)
    description =Column(String(1024), nullable=True)
    image_id = Column(String(60), ForeignKey('files.id'), nullable=True)
    target = Column(String(60), ForeignKey('courses.id'), nullable=True)
    deadline = Column(DateTime)

    course = relationship('Course', back_populates='event')
    file = relationship('File', back_populates='event')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

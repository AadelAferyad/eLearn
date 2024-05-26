#!/usr/bin/python3
from models.base_models import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship



class Lesson(BaseModel, Base):
    """
        lesson class
    """

    __tablename__ = 'lessons'
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=False)
    file_id = Column(String(60), ForeignKey('files.id'), nullable=True)
    target = Column(String(60), ForeignKey('courses.id'), nullable=False)
    deadline = Column(DateTime, nullable=False)

    file = relationship('File', back_populates='lesson')
    course = relationship('Course', back_populates='lesson')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

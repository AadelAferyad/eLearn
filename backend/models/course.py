#!/usr/bin/python3
"""
    this file is for the course class
"""

from models.base_models import BaseModel, Base

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Course(BaseModel, Base):
    """
        courses class this class is for course tables
    """

    __tablename__ = 'courses'
    name = Column(String(60), nullable=False)
    year = Column(Integer, nullable=False)

    teacher = relationship('Teacher', back_populates='course')
    student = relationship('Student', back_populates='course')
    event = relationship('Event', back_populates='course')
    lesson = relationship('Lesson', back_populates='course')
    resource = relationship('Resource', back_populates='course')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

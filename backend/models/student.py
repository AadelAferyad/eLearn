#!/usr/bin/python3
"""
    this file is for student class
"""

from models.base_models import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """
        Student class
    """

    __tablename__ = 'students'
    person_id = Column(String(60), ForeignKey('persons.id'))
    course_id = Column(String(60), ForeignKey('courses.id'))

    person = relationship('Person', back_populates='student')
    course = relationship('Course', back_populates='student')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

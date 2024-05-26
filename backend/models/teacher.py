#!/usr/bin/python3
from models.base_models import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Teacher(BaseModel, Base):
    """
        Teacher table
    """

    __tablename__ = 'teachers'
    person_id = Column(String(60), ForeignKey('persons.id'))
    course_id = Column(String(60), ForeignKey('courses.id'))

    course = relationship('Course', back_populates='teacher')
    person = relationship('Person', back_populates='teacher')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#!/usr/bin/python3
"""
    this file is for resources class
"""

from models.base_models import BaseModel, Base

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Resource(BaseModel, Base):
    """
       resource class
    """

    __tablename__ = 'resources'
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=False)
    file_id = Column(String(60), ForeignKey('files.id'), nullable=True)
    target = Column(String(60), ForeignKey('courses.id'), nullable=False)

    file = relationship('File', back_populates='resource')
    course = relationship('Course', back_populates='resource')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

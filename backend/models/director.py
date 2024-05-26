#!/usr/bin/python3
from models.base_models import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class Director(BaseModel, Base):
    """ director class """
    __tablename__ = 'directors'
    person_id = Column(String(60), ForeignKey('persons.id'))
    person = relationship('Person', back_populates='director')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#!/usr/bin/python3
from models.base_models import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class File(BaseModel, Base):
    """ this class for (file, images, pdf ...)
    all other tables that need files will be here in this table
    """

    __tablename__ = 'files'
    name = Column(String(80), nullable=True)
    path = Column(String(256), nullable=False)

    person = relationship('Person', back_populates='image')
    event = relationship('Event', back_populates='file')
    lesson = relationship('Lesson', back_populates='file')
    resource = relationship('Resource', back_populates='file')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
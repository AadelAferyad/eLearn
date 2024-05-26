#!/usr/bin/python3
from models.base_models import BaseModel, Base
from sqlalchemy import String, ForeignKey, Column, Date
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class Person(BaseModel, Base):
    """ Person class, all the common attributes the individuals shares """

    __tablename__ = 'persons'
    first_name = Column(String(60), nullable=False)
    last_name = Column(String(60), nullable=False)
    email = Column(String(256), nullable=True)
    phone = Column(String(20), nullable=True)
    username = Column(String(60), nullable=False)
    password = Column(String(256), nullable=False)
    birthday = Column(Date, nullable=True)
    image_id = Column(String(256), ForeignKey('files.id'))

    director = relationship('Director', back_populates='person')
    image = relationship('File', back_populates='person')
    teacher = relationship('Teacher', back_populates='person')
    student = relationship('Student', back_populates='person')

    def __init__(self, **kwargs):
        if 'password' in kwargs:
            self.password = generate_password_hash(kwargs['password'])
            del kwargs['password']
        super().__init__(**kwargs)

    def check_password(self, password):
        return check_password_hash(self.password, password)

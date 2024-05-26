#!/usr/bin/python3

from os import getenv
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.base_models import Base
from models.person import Person
from models.file import File
from models.director import Director
from models.teacher import Teacher
from models.course import Course
from models.student import Student
from models.event import Event
from models.lesson import Lesson
from models.resources import Resource


load_dotenv()


class DBStorage:
    """ storage class """
    
    __engine = None
    __session = None

    def __init__(self):
        url = getenv('DATABASE_URL')
        self.__engine = create_engine(url)

    def get(self, obj, id=None):
        if id and obj:
            return self.__session.query(obj).get(id)
        return self.__session.query(obj).all()

    def get_by_name(self, obj, name):
        return self.__session.query(obj).filter_by(name=name).all()


    def reload(self):
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    #user method
    def check_username(self, username):
        return self.__session.query(Person).filter_by(username=username).first()



    def close(self):
        self.__session.remove()



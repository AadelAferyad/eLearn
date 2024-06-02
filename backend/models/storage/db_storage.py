#!/usr/bin/python3
"""
this file is for database storage
creates database and handles CRUD opirations 
"""

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
    """
        DBStorage is a class used to interact with the database using SQLAlchemy.

        This class handles the connection to the database, allows for session management, 
        and provides methods for CRUD operations and queries.
    """
    
    __engine = None
    __session = None

    def __init__(self):
        """
            Initializes the DBStorage instance by creating an SQLAlchemy engine.

            The engine is created using the database URL from the environment variables.
        """
        url = getenv('DATABASE_URL')
        self.__engine = create_engine(url)


    def reload(self):
        """
            Creates all tables in the database and initializes a new session.

            This method uses the metadata of the Base class to create all tables and sets up a scoped session.
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)

    def new(self, obj):
        """
            Adds a new object to the current session.

            Parameters:
            ----------
            obj : SQLAlchemy model instance
                The object to be added to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
            Commits (saves) the current session to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Deletes an object from the current session if it exists.

            Parameters:
            ----------
            obj : SQLAlchemy model instance, optional
                The object to be deleted from the session. If None, no action is taken.
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
            Closes the current session.

            This method removes the current session, ensuring all changes are committed and the session is closed properly.
        """
        self.__session.remove()

    def get(self, obj, id=None):
        """
            Retrieves an object by its class and ID or retrieves all objects of the class.

            Parameters:
            ----------
            obj : SQLAlchemy model class
                The class of the object(s) to retrieve.
            id : str (uuid8), optional
                The ID of the object to retrieve. If None, retrieves all objects of the class.

            Returns:
            -------
            SQLAlchemy model instance or list
                The object(s) retrieved from the database.
        """
        if id:
            return self.__session.query(obj).get(id)
        return self.__session.query(obj).all()

    def get_by_name(self, obj, name=None, year=None):
        """
            Retrieves objects by their name and optionally by year.

            Parameters:
            ----------
            obj : SQLAlchemy model class
                The class of the object(s) to retrieve.
            name : str, optional
                The name of the object(s) to retrieve.
            year : int, optional
                The year associated with the object(s) to retrieve.

            Returns:
            -------
            list
                The object(s) retrieved from the database.
        """
        if year and name:
            return self.__session.query(obj).filter_by(name=name).filter_by(year=year).all()
        elif name:
            return self.__session.query(obj).filter_by(name=name).all()
        return self.__session.query(obj).all()

    def check_username(self, username):
        """
            Checks if a username exists in the Person table.

            Parameters:
            ----------
            username : str
                The username to check.

            Returns:
            -------
            Person instance or None
                The person with the specified username, or None if not found.
        """
        return self.__session.query(Person).filter_by(username=username).first()

    def role(self, obj, id):
         """
            Retrieves a role (Student/Teacher/Director) for a person by their person_ID.

            Parameters:
            ----------
            obj : SQLAlchemy model class
                The class of the role to retrieve.
            id : str(uuid8)
                The ID of the person whose role is to be retrieved.

            Returns:
            -------
            SQLAlchemy model instance
                The role associated with the person.
        """
        return self.__session.query(obj).filter_by(person_id=id).first()

    def count(self, obj):
         """
            Counts the number of objects of a given class.
            
            Parameters:
            ----------
            obj : SQLAlchemy model class
                The class of the objects to count.
            
            Returns:
            -------
            int
                The number of objects in the database of the specified class.
        """
        list_obj = self.get(obj)
        return len(list_obj)
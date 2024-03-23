#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Create tables in the environment"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@{host}/{db}', pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of objects"""
        result = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for c in classes:
                query = self.__session.query(c)
                for obj in query:
                    key = f"{type(obj).__name__}.{obj.id}"
                    result[key] = obj
        return result

    def new(self, obj):
        """Add a new element to the session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an element from the session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Configure and create tables"""
        Base.metadata.create_all(bind=self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session"""
        self.__session.close()

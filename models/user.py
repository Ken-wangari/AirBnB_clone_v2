#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Class representing a user"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", cascade="all, delete, delete-orphan", backref="user")
    reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="user")


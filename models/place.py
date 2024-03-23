#!/usr/bin/python3
"""The place class"""
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex
from models.base_model import BaseModel, Base

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                      Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """Class representing a Place"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns the list of reviews"""
            return [review for review in models.storage.all(Review).values() if review.place_id == self.id]

        @property
        def amenities(self):
            """Returns the list of amenity_ids"""
            return [amenity_id for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj=None):
            """Appends amenity ids to the attribute"""
            if obj and obj.__class__.__name__ == "Amenity":
                self.amenity_ids.append(obj.id)


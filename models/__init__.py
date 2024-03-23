#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.city import City
from os import getenv


storage_type = os.getenv("HBNB_TYPE_STORAGE", "file")

if storage_type == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

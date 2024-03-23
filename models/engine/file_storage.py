#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self, cls=None):
        if cls:
            return {key: obj for key, obj in self.__objects.items() if isinstance(obj, cls)}
        else:
            return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = globals()[class_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        self.reload()

class BaseModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)

    def to_dict(self):
        return {'__class__': type(self).__name__, 'id': self.id}

class User(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class State(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class City(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Amenity(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Place(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Review(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()


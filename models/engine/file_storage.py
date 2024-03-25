#!/usr/bin/python3
""" This is a file storage that serializes an instance to a JSON file (JSON.dump)
    It also deserializes a JSON file to an instance (JSON.load)
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review



class FileStorage:
    """This class serializes instance to a JSON file and deserializes JSON to instance"""
    __file_path = "file.json" #string - path to the JSON file (ex: file.json)
    __objects = {} #empty dict, but it will store all objects by <class name>.id

    def all(self):
        """This returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id
            all it does is to get the key of the form <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """This serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}

        """Next, fill dictionary with an __objects element"""
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    
    def reload(self):
        """THis deserializes the JSON file to __objects"""
        try:
            """ if the JSON file (__file_path) exists"""
            with open(self.__file_path, 'r', encoding="UTF8") as file:
                for key, value in json.load(file).items():
                    attr_value = eval(value["__class__"])(**value)
                    self.__objects[key] = attr_value
        except FileNotFoundError:
            pass



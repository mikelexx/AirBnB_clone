#!/usr/bin/env python3
"""
This module deals with file storage of instances.
"""
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import os


class FileStorage():
    """
    This class serializes instances to a JSON file and deserializes
    JSON file file instances.
    """
    __file_path = "file.json"
    __objects: dict = {}

    def all(self):
        """
        returns: the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Args:
            objs: instance to be included in __objects.
        """
        key = obj.__class__.__name__
        key += "."
        key += obj.id

        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_rep_of_obj = {}
        for key, obj in FileStorage.__objects.items():
            dict_rep_of_obj[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(dict_rep_of_obj, f)

    def reload(self):
        """
         deserializes the JSON file to python objects __objects (
         only if the JSON
         file (__file_path) exists ; otherwise, do nothing.
         Json file contains json objects not json formated string, thats
         why i use json load instead of loads.
         If the file doesn’t exist, no exception should be raised)
         """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
            json_serialized_objects = json.load(f)
            for key, val in json_serialized_objects.items():
                FileStorage.__objects[key] = eval(val['__class__'])(**val)

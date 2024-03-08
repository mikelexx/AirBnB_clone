#!/usr/bin/env python3
"""
This module contains class that defines all common attributes\
        for other classes.
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    This class defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        if kwargs and len(kwargs) > 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        self.__dict__[key] = datetime.strptime(
                                val, "%Y-%m-%dT%H:%M:%S.%f")
                    else:
                        self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        new_dict = dict(self.__dict__)
        for key, val in self.__dict__.items():
            if key == "created_at":
                new_dict[key] = self.created_at.isoformat()
            elif key == "updated_at":
                new_dict[key] = self.updated_at.isoformat()
            elif key == "id":
                new_dict[key] = self.id
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

#!usr/bin/env python3
"""
This module contains unittests for filestorage engine
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """
    THis class contains testcases for file_storage engine
    """

    def test__init__(self):
        """
        test initialization of filestorage works correctly
        """
        file_storage = FileStorage()
        self.assertTrue(type(file_storage), FileStorage)

    def test_attributes(self):
        """
        asserts all the attributes required are present
        """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "__init__"))

    def test_all(self):
        """
        test the all method of FileStorage class
        It also tests save method correctly saves an object in json file
        in the process
        """
        file_storage = FileStorage()
        self.assertIs(type(file_storage.all()), dict)
        city = City()
        city.save()
        place = Place()
        place.save()
        user = User()
        user.save()
        amenity = Amenity()
        amenity.save()
        state = State()
        state.save()
        review = Review()
        review.save()
        base = BaseModel()
        base.save()
        for key, val in file_storage.all().items():
            self.assertIn(type(val), [
                BaseModel, Place, User, City, Amenity, Review, State])

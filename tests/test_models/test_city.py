#!/usr/bin/env python3
"""
This module contains class for testing City model
"""
from models.city import City
from models.base_model import BaseModel
import unittest
import os


class TestCity(unittest.TestCase):
    """
    This class tests City model
    """
    @classmethod
    def setUpClass(cls):
        """
        for making sure we don't change original the file
        contents while testing
        """
        try:
            os.rename("file.json", "original_file")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """
        for setting binding back data orginal storage to the application
        after tests with temporary dat storage file have been finished
        and deleting the temporary file that was used.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("original_file", "file.json")
        except IOError:
            pass

    def test__init__(self):
        """
        tests initialization of city model.
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """
        tests for existence of certain required attributes
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertIs(type(city.state_id), str)
        self.assertTrue(hasattr(city, "name"))
        self.assertIs(type(city.name), str)
        self.assertTrue(hasattr(city, "to_dict"))
        self.assertTrue(hasattr(city, "save"))
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_to_dict(self):
        """tests the to_dict method of city model"""
        city = City()
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)

    def test_save(self):
        """ tests the save method of city model"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)

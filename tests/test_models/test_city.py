#!/usr/bin/env python3
"""
This module contains class for testing City model
"""
from models.city import City
from models.base_model import BaseModel
import unittest


class TestCity(unittest.TestCase):
    """
    This class tests City model
    """
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

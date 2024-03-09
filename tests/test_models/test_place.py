#!/usr/bin/env python3
"""
THis module contains unittest for Place model
"""
from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """
    THis class tests the Place Model
    """

    def test__init__(self):
        place = Place()
        place.name = "Nairobi"
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_correct_attributes(self):
        """
        tests that place model has required attributes with correct type
        """
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertIs(type(place.city_id), str)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertIs(type(place.longitude), float)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertIs(type(place.latitude), float)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertIs(type(place.price_by_night), int)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertIs(type(place.max_guest), int)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertIs(type(place.number_bathrooms), int)
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertIs(type(place.number_rooms), int)
        self.assertTrue(hasattr(place, "description"))
        self.assertIs(type(place.description), str)
        self.assertTrue(hasattr(place, "name"))
        self.assertIs(type(place.name), str)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertIs(type(place.amenity_ids), list)
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "to_dict"))
        self.assertTrue(hasattr(place, "save"))

    def test_save(self):
        """ tests the save method of place model"""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)

    def test_to_dict(self):
        """tests the to_dict method of ple model"""
        place = Place()
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)

    def test_function_docs(self):
        """
        tests that all functions of place model are documented
        """
        self.assertIsNotNone(Place.__doc__)

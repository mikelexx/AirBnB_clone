#!/usr/bin/env python3
"""
This module contains class for testing Amenity model
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import os


class TestAmenity(unittest.TestCase):
    """
    This class tests Amenity model
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
        tests initialization of amenity model.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """
        tests for existence of certain required attributes
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertIs(type(amenity.name), str)
        self.assertTrue(hasattr(amenity, "to_dict"))
        self.assertTrue(hasattr(amenity, "save"))
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_to_dict(self):
        """tests the to_dict method of amenity model"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_save(self):
        """ tests the save method of amenity model"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)

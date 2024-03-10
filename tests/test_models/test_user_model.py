#!/usr/bin/env python3
"""
This module contains class for testing User model
"""
from models.user import User
from models.base_model import BaseModel
import unittest
import os


class TestUser(unittest.TestCase):
    """
    This class tests User model
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
        tests initialization of user model.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """
        tests for existence of certain required attributes
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertIs(type(user.email), str)
        self.assertTrue(hasattr(user, "password"))
        self.assertIs(type(user.password), str)
        self.assertTrue(hasattr(user, "first_name"))
        self.assertIs(type(user.first_name), str)
        self.assertTrue(hasattr(user, "last_name"))
        self.assertIs(type(user.last_name), str)
        self.assertTrue(hasattr(user, "to_dict"))
        self.assertTrue(hasattr(user, "save"))
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_to_dict(self):
        """tests the to_dict method of user model"""
        user = User()
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)

    def test_save(self):
        """ tests the save method of user model"""
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

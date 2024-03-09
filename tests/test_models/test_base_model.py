#!/usr/bin/python3
"""
This module contains test for the base_model module's
class and methods
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
import json


class TestBaseModel(unittest.TestCase):
    """
    Tests the BaseModel class and its functions
    """
    def setUp(cls):
        """
        sets up temporary instances for testing
        """

    def test_init__(self):
        """
        asserts creation of new unique instances and existence
        all the required attributes
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "__str__"))

    def test_initialization_with_kwargs(self):
        """
        Asserts that initialization with keyword arguments is handled.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(new_model_dict['id'], my_model.id)
        self.assertEqual(new_model_dict['name'], my_model.name)
        self.assertEqual(new_model_dict['my_number'], my_model.my_number)
        self.assertEqual(new_model_dict[
            '__class__'], my_model.__class__.__name__)

    def test_public_instance_attributes(self):
        """
        tests that the instance attributes are set propery.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertNotEqual(str(my_model.created_at), str(my_model.updated_at))
        self.assertIsInstance(my_model.my_number, int)
        self.assertEqual(my_model.my_number, 89)

    def test_save(self):
        """
        Asserts the updated_at property of objected changes
        when object is updated
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)
        self.assertIn(my_model, FileStorage().all().values())

    def test_to_dict(self):
        """
        Tests that object is converted to dictionary type
        """
        my_model = BaseModel()
        my_model.my_number = 89
        to_dict = my_model.to_dict()
        self.assertIsInstance(to_dict, dict)
        self.assertIsInstance(to_dict['__class__'], str)
        self.assertIsInstance(to_dict['created_at'], str)
        self.assertIsInstance(to_dict['updated_at'], str)
        self.assertIsInstance(to_dict['my_number'], int)
        self.assertEqual(to_dict['__class__'], 'BaseModel')
        self.assertEqual(to_dict['id'], my_model.id)
        self.assertEqual(to_dict['my_number'], 89)
        dict_created_at_rep = to_dict['created_at'].split('T')
        self.assertEqual(" ".join(dict_created_at_rep), str(
            my_model.created_at))
        dict_updated_at_rep = to_dict['updated_at'].split('T')
        self.assertEqual(" ".join(dict_updated_at_rep), str(
            my_model.updated_at))

    def test_invalid_input_to_methods(self):
        """
        tests that type error is raised for invalid input to methods
        """
        my_model = BaseModel()
        self.assertRaises(TypeError, my_model.save, "invalid input")
        self.assertRaises(TypeError, my_model.to_dict, "invalid input")

    def test__str__(self):
        pass

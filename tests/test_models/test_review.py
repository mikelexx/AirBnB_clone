#!/usr/bin/env python3
"""
This module contains class for testing Review model
"""
from models.review import Review
from models.base_model import BaseModel
import unittest
import os


class TestReview(unittest.TestCase):
    """
    This class tests Review model
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
        tests initialization of review model.
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """
        tests for existence of certain required attributes
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertIs(type(review.place_id), str)
        self.assertTrue(hasattr(review, "text"))
        self.assertIs(type(review.text), str)
        self.assertTrue(hasattr(review, "to_dict"))
        self.assertTrue(hasattr(review, "save"))
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_to_dict(self):
        """tests the to_dict method of review model"""
        review = Review()
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)

    def test_save(self):
        """ tests the save method of review model"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)

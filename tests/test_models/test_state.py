#!/usr/bin/env python3
"""
This module contains class for testing State model
"""
from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
    """
    This class tests State model
    """
    def test__init__(self):
        """
        tests initialization of state model.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """
        tests for existence of certain required attributes
        """
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertIs(type(state.name), str)
        self.assertTrue(hasattr(state, "to_dict"))
        self.assertTrue(hasattr(state, "save"))
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_to_dict(self):
        """tests the to_dict method of state model"""
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_save(self):
        """ tests the save method of state model"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

#!/usr/bin/python3
"""
The State test class
"""

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_init(self):
        """
        Test the initialization of State objects.

        Ensure that State objects are properly initialized with the correct
        types for id, created_at, and updated_at attributes.
        """
        state = State()
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of State objects.

        Ensure that the __str__ method of State objects returns a string
        containing the class name, id, created_at, and updated_at attributes.
        """
        state = State()
        state_str = str(state)
        self.assertIn("[State]", state_str)
        self.assertIn("id", state_str)
        self.assertIn("created_at", state_str)
        self.assertIn("updated_at", state_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of State objects with keyword arguments.

        Ensure that State objects can be initialized with the correct
        values for id, created_at, updated_at, and name attributes using
        keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'name': 'Test State'
        }
        state = State(**data)
        self.assertEqual(state.id, '123')
        self.assertEqual(state.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(state.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(state.name, 'Test State')

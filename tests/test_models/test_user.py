#!/usr/bin/python3
"""
Test for User
"""

import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """
    The test class
    """

    def test_init(self):
        """
        Test the initialization of User objects.

        Ensure that User objects are properly initialized with the correct
        types for id, created_at, and updated_at attributes.
        """
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of User objects.

        Ensure that the __str__ method of User objects returns a string
        containing the class name, id, created_at, and updated_at attributes.
        """
        user = User()
        user_str = str(user)
        self.assertIn("[User]", user_str)
        self.assertIn("id", user_str)
        self.assertIn("created_at", user_str)
        self.assertIn("updated_at", user_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of User objects with keyword arguments.

        Ensure that User objects can be initialized with the correct values
        for id, created_at, updated_at, email, password, first_name, and
        last_name attributes using keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        user = User(**data)
        self.assertEqual(user.id, '123')
        self.assertEqual(user.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(user.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

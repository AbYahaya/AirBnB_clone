#!/usr/bin/python3
"""
A test for amenity
"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_init(self):
        """
        Test the initialization of Amenity objects.

        Ensure that Amenity objects are properly initialized with the
        correct types for id, created_at, and updated_at attributes.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of Amenity objects.

        Ensure that the __str__ method of Amenity objects returns a
        string containing the class name, id, created_at, and updated_at
        attributes.
        """
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIn("[Amenity]", amenity_str)
        self.assertIn("id", amenity_str)
        self.assertIn("created_at", amenity_str)
        self.assertIn("updated_at", amenity_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of Amenity objects with keyword arguments.

        Ensure that Amenity objects can be initialized with the correct
        values for id, created_at, updated_at, and name attributes
        using keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'name': 'Test Amenity'
        }
        amenity = Amenity(**data)
        self.assertEqual(amenity.id, '123')
        self.assertEqual(amenity.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(amenity.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(amenity.name, 'Test Amenity')

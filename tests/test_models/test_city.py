#!/usr/bin/python3
"""
Tests for the City class
"""

import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_init(self):
        """
        Test the initialization of City objects.

        Ensure that City objects are properly initialized with the correct
        types for id, created_at, and updated_at attributes.
        """
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of City objects.

        Ensure that the __str__ method of City objects returns a string
        containing the class name, id, created_at, and updated_at attribute.
        """
        city = City()
        city_str = str(city)
        self.assertIn("[City]", city_str)
        self.assertIn("id", city_str)
        self.assertIn("created_at", city_str)
        self.assertIn("updated_at", city_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of City objects with keyword arguments.

        Ensure that City objects can be initialized with the correct values
        for id, created_at, updated_at, state_id, and name attributes
        using keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'state_id': '456',
            'name': 'Test City'
        }
        city = City(**data)
        self.assertEqual(city.id, '123')
        self.assertEqual(city.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(city.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(city.state_id, '456')
        self.assertEqual(city.name, 'Test City')

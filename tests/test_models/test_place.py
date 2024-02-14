#!/usr/bin/python3
"""
Test for Place
"""

import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_init(self):
        """
        Test the initialization of Place objects.

        Ensure that Place objects are properly initialized with the
        correct types for id, created_at, and updated_at attributes.
        """
        place = Place()
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of Place objects.

        Ensure that the __str__ method of Place objects returns a string
        containing the class name, id, created_at, and updated_at attributes.
        """
        place = Place()
        place_str = str(place)
        self.assertIn("[Place]", place_str)
        self.assertIn("id", place_str)
        self.assertIn("created_at", place_str)
        self.assertIn("updated_at", place_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of Place objects with keyword arguments.

        Ensure that Place objects can be initialized with the correct
        values for id, created_at, updated_at, city_id, user_id, name,
        description, number_rooms, number_bathrooms, max_guest,
        price_by_night, latitude, longitude, and amenity_ids attributes
        using keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'city_id': '456',
            'user_id': '789',
            'name': 'Test Place',
            'description': 'Test description',
            'number_rooms': 2,
            'number_bathrooms': 1,
            'max_guest': 4,
            'price_by_night': 100,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['1', '2', '3']
        }
        place = Place(**data)
        self.assertEqual(place.id, '123')
        self.assertEqual(place.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(place.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.user_id, '789')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'Test description')
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['1', '2', '3'])

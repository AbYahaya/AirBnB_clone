#!/usr/bin/python3
"""
A test module
"""

import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_init(self):
        """
        Test the initialization of Review objects.

        Ensure that Review objects are properly initialized with the correct
        types for id, created_at, and updated_at attributes.
        """
        review = Review()
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_str(self):
        """
        Test the string representation of Review objects.

        Ensure that the __str__ method of Review objects returns a string
        containing the class name, id, created_at, and updated_at attributes.
        """
        review = Review()
        review_str = str(review)
        self.assertIn("[Review]", review_str)
        self.assertIn("id", review_str)
        self.assertIn("created_at", review_str)
        self.assertIn("updated_at", review_str)

    def test_init_with_kwargs(self):
        """
        Test initialization of Review objects with keyword arguments.

        Ensure that Review objects can be initialized with the correct value
        s for id, created_at, updated_at, place_id, user_id, and text
        attributes using keyword arguments.
        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000',
            'place_id': '456',
            'user_id': '789',
            'text': 'Test review'
        }
        review = Review(**data)
        self.assertEqual(review.id, '123')
        self.assertEqual(review.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(review.updated_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Test review')

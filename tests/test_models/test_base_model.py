#!/usr/bin/python3
"""
Test module for base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class containing testcases for functions
    """

    def test_init(self):
        """

        """
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """

        """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("id", model_str)
        self.assertIn("created_at", model_str)
        self.assertIn("updated_at", model_str)

    def test_save(self):
        """

        """
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict(self):
        """

        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_init_with_kwargs(self):
        """

        """
        data = {
            'id': '123',
            'created_at': '2024-02-14T12:00:00.000000',
            'updated_at': '2024-02-14T12:00:00.000000'
        }
        model = BaseModel(**data)
        self.assertEqual(model.id, '123')
        self.assertEqual(model.created_at, datetime(2024, 2, 14, 12, 0))
        self.assertEqual(model.updated_at, datetime(2024, 2, 14, 12, 0))

#!/usr/bin/python3
"""
This holds all test cases for FileStorage
"""

import unittest
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    @classmethod
    def setUpClass(cls):
        cls.file_path = 'test_storage.json'
        cls.file_storage = FileStorage()
        cls.file_storage._FileStorage__file_path = cls.file_path

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.file_path):
            os.remove(cls.file_path)

    def tearDown(self):
        self.file_storage._FileStorage__objects = {}

    def test_all(self):
        """
        Test the all method of FileStorage class.

        Ensure that the all method returns the dictionary of objects.
        """
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """
        Test the new method of FileStorage class.

        Ensure that the new method adds an object to the __objects
        attribute of FileStorage class.
        """
        data = {'id': '123'}
        obj = type('TestObj', (), data)
        self.file_storage.new(obj)
        self.assertIn('TestObj.123', self.file_storage._FileStorage__objects)

    def test_save(self):
        """
        Test the save method of FileStorage class.

        Ensure that the save method serializes the __objects attribute
        into a JSON file.
        """
        data = {'id': '123'}
        obj = type('TestObj', (), data)
        self.file_storage.new(obj)
        self.file_storage.save()
        self.assertTrue(os.path.exists(self.file_path))
        with open(self.file_path, 'r') as f:
            saved_data = json.load(f)
            self.assertIn('TestObj.123', saved_data)

    def test_reload(self):
        """
        Test the reload method of FileStorage class.

        Ensure that the reload method deserializes the JSON file into the _
        _objects attribute.
        """
        data = {'id': '123'}
        with open(self.file_path, 'w') as f:
            json.dump({'TestObj.123': data}, f)
        self.file_storage.reload()
        self.assertIn('TestObj.123', self.file_storage._FileStorage__objects)

#!/usr/bin/python3
"""
This serializes and deserializes
It was created by Yahaya Abdulrauf:
    2/10/2024
"""
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'json.file'
    __objects = dict()

    def __init__(self):
        """
        The init method of the class

        """
        pass

    def all(self):
        """"
        Returns the dictionary __objects

        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Creates a new object and add to the Class var __objects using key
        """

        new_dict = obj.to_dict()
        key = '{}.{}'.format(new_dict['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        holder_dict = dict()
        for key, value in FileStorage.__objects.items():
            holder_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as jsonfile:
            json.dump(holder_dict, jsonfile)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file\
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t\
        exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, 'r') as objfile:
                obj_holder = json.load(objfile)
            for key, value in obj_holder.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except:
            pass

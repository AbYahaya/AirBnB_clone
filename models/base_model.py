#!/usr/bin/python3
"""
    This is the BaseModel from which other classes will will inherit

    This was made by Yahaya Abdulrauf:
    Date: 2/9/2024

"""
import uuid
import models
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        The init method of this class
        args - tuple of arguments passed into the function
        kwargs - dict of args

        """

        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime\
                            .strptime(value, '%Y-%m-%dT%H:%M:%S.%f')

                elif key == 'id':
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Strin formated output of the class,id and dictionaries
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Gives time of last update
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary of the instance

        obj_dict -  holds a copy of the dictionary of the instance
        obj_dict['__class__'] - a key to hold the name of the\
                instances class

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

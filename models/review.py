#!/usr/bin/python3
"""
Created by Yahaya Abdulrauf
2/13/2024
"""

from models.base_model import BaseModel


class Review(Basemodel):
    place_id = ""
    user_id = ""
    text = ""
    """
    A cass that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        the init method of this clss
        """
        super().__init__(*args, **kwargs)

#!/usr/bin/python3
"""
Created by Yahaya Abdulrauf
2/13/2024
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This classinherits from Basemodel
    """
    state_id = ""
    name = ""
    def __init__(self, *args, **kwargs):
        """
        The init method of this class
        """

        super().__inti__(*args, **kwargs)

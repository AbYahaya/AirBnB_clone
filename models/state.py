#!/usr/bin/python3
"""
Another model that will inherit from BaseModel
Created on 2/12/2024 by Yahaya Abdulrauf
"""


class State(BasModels):
    name = ""

    def __int__(self, *args, **kwargs):
        """
        The init method of the State class
        It has:
        Args: A tuple of arguments
        Kwargs: A dict of arguments to the function
        """

        super().__init__(*args, **kwargs)

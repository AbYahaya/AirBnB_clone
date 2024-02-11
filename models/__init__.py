#!/usr/bin/python3
"""
This makes the models directory a python packag

it was created by Yahaya ABdulrauf:
    2/11/2024
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

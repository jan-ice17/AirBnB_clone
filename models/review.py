#!/usr/bin/python
"""A class Review that is inherited from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
    
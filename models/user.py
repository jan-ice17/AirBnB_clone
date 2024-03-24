#!/usr/bin/python3
"""A class User thatis inherited from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
     """class 
     that inherits from BaseModel"""
     email = ""
     password = ""
     first_name = ""
     last_name = ""
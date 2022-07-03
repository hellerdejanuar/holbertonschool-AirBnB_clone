#!/usr/bin/python3
"""
User Base Module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

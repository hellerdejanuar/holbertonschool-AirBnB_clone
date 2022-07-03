#!/usr/bin/python3
"""
Review Base Module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review
    """
    text = ""
    place_id = ""  # empty string but it will be Place.id
    user_id = ""  # empty string but it will be User.id

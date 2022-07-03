#!/usr/bin/python3
"""
City Base Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City
    """
    name = ""
    state_id = ""  # empty. it will be the State.id

#!/usr/bin/python3
"""
Place Base Module
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place
    """
    name = ""
    city_id = ""  # empty string but it will be City.id
    user_id = ""  # empty string but it will be User.id
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # empty list but will have Amenity.id

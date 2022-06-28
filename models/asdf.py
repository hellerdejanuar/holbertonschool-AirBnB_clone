#!/usr/bin/python3
""" Base Model """
import json
from datetime import datetime
import uuid

class BaseModel():
    """ Base Class """


    def __init__(self):
        """ Initializator """
        self.id = str(uuid.uuid4()) 
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Print string method """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ Save changes and update updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a key/value dictionary """
        return {'id': self.id, 'created_at': self.created_at.isoformat('T', 'auto'),
                'updated_at': self.updated_at.isoformat('T', 'auto'), '__class__': self.__class__.__name__}

#!/usr/bin/python3
""" Base Model """
import json
from datetime import datetime
import uuid


class BaseModel():
    """ Base Class """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                if key != '__class__':
                    if (key == 'created_at' or  key == 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])
        else:
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
        return_dict = self.__dict__
        return_dict['created_at'] = self.created_at.isoformat()
        return_dict['updated_at'] = self.updated_at.isoformat()
        return_dict.update({'__class__' : self.__class__.__name__})
        return return_dict

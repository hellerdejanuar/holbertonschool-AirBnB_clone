#!/usr/bin/python3
""" Base Model """
import json
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """ Base Class """

    def __init__(self, *args, **kwargs):
        """ Initializator of Base Model """
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key != '__class__':
                    if (key == 'created_at' or  key == 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """ Print string method """
        dic = {k: self.__dict__[k] for k in self.__dict__ if k != '__class__'}
        # removes __class__ attribute from auxiliary dic
        return (f"[{self.__class__.__name__}] ({self.id}) {dic}")

    def save(self):
        """ Save changes and update updated_at """
        storage.save()
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def to_dict(self):
        """ Returns a key/value dictionary """
        #return_dict = self.__dict__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        #return_dict.update({'__class__' : self.__class__.__name__})
        return self.__dict__

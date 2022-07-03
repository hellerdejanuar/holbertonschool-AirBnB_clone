#!/usr/bin/python3
"""
Base Model - Base for all other classes to inherit from
Serialization-Deserialization process with JSON
"""
import json
from datetime import datetime
import uuid
from models import storage


class BaseModel():
    """
    Base Class: defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializator of Base Model
        Attributes:
            id: string - assign with an uuid when an instance is created
            created_at: datetime - assign with the current
                        datetime when an instance is created
            updated_at: datetime - assign with the current datetime
                        when an instance is created and it will be updated
                        every time you change your object

        Arguments:
            *args: isn't used
            **kwargs: dictionary that contains all arguments by key/value
        """
        if kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key != '__class__':
                    if (key == 'created_at' or key == 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(kwargs[key]))
                    else:
                        setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        Print string method
        """
        dic = {k: self.__dict__[k] for k in self.__dict__ if k != '__class__'}
        # removes __class__ attribute from auxiliary dic
        return (f"[{self.__class__.__name__}] ({self.id}) {dic}")

    def save(self):
        """
        Save changes and update updated_at
        """
        self.updated_at = datetime.now()
        storage.save()
        # self.created_at = datetime.now() # is this really needed??

    def to_dict(self):
        """
        Returns a key/value dictionary
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        # new_dict.update({'__class__' : self.__class__.__name__})
        return new_dict

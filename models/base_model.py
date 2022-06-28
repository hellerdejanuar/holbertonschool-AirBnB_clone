#!/usr/bin/python3
""" base model """

class BaseModel:
    
    def __init__(self):
        id = #assign with an uuid CASTED TO STR when created (unique uid for each)
        created_at =
        updated_at =

    def __str__(self):
        classname, self id, self __dict__

    def save(self):
        updated_at = now()

    def to_dict(self):
    #???? return the __dict with all the keys + __class__ key with the name of the class + updated_at and created_at must be co0nverted to string using ISO format

        return self.__dict__.update({'__clas__': self.__class__}) 



#!/usr/bin/python3
""" Engine Module """
import json


class FileStorage():
    """ Class FileStorage """

    __file_path = "file.json" #path to the JSON file (ex: file.json)
    __objects = {} #dict type. empty but will store all objects by <class name>.id

    def __init__(self):
      	""" Initializator of FileStorage Instance """

    def all(self):
    	""" Returns the dictionary __objects """
    	return self.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id"""
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj.to_dict()})

    def save(self):
        """ Serializes __objects to the JSON file """
        if self.__file_path:
            with open(self.__file_path, 'w') as f:
                f.write(json.dumps(self.__objects))
        else:
            self.__objects = {}

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
                {self.__objects.update(json.loads(dic)) for dic in f}
        except FileNotFoundError:
            return

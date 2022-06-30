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
    	return __object.update({f'{obj.__class__.__name__}.{obj.id}': obj})

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(__objects))

    def reload(self):
        """ Deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as f:
            #    __objects_copy = json.loads(f.read())
            # return [__objects.update(**dic) for dic in __objects]
                return [FileStorage.__objects.update(json.loads(dic)) for dic in f]
        except FileNotFoundError:
            return

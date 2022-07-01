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
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        #self.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj.to_dict()})

    def save(self):
        """ Serializes __objects to the JSON file """
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
            json.dump(self.__objects, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        classes = {'BaseModel': BaseModel, 'User': User}
        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
                for key, value in self.__objects.items():
                    self.__objects[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass
        #try:
        #    with open(self.__file_path, 'r') as f:
        #        {self.__objects.update(json.loads(dic)) for dic in f.read()}
        #except FileNotFoundError:
        #    return

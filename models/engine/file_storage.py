#!/usr/bin/python3
"""
Engine Module
"""
import json


class FileStorage():
    """
    Class FileStorage: serializes instances to a JSON file
                    and deserializes JSON file to instances
    Private Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - will store all objects by <class name>.id
    Public instance methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects
    """

    __file_path = "file.json"  # path to the JSON file (ex: file.json)
    __objects = {}  # dict empty but will store all objects by <class name>.id

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
# self.__objects.update({f"{obj.__class__.__name__}.{obj.id}" : obj.to_dict()})

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        from models.base_model import BaseModel
# temp = {key: value.to_dict() for key, value in self.__objects.items()}
        temp = self.__objects.copy()
        for key, value in temp.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(temp, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel

        try:
            with open(self.__file_path, 'r') as f:
                self.__objects = json.loads(f.read())
                for key, value in self.__objects.items():
                    self.__objects[key] = FileStorage.classes()[value[
                                            '__class__']](**value)
# self.__objects = {k: classes[v['__class__']](**v)
# for k, v in self.__objects.items()}
        except FileNotFoundError:
            pass
        #    with open(self.__file_path, 'r') as f:
        #        {self.__objects.update(json.loads(dic)) for dic in f.read()}

    @staticmethod
    def classes():
        """
        Returns a dict of classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        return classes_dict

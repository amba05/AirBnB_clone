#!/usr/bin/python3
'''
    Define class FileStorage
'''

import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.

        Attributes:
            __file_path (str): The name of the file to save objects to.
            __objects (dict): A dictionary of instantiated objects.
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            Return the dictionary
        '''
        return type(self).__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            (Basically this function gets the cls name of the passed obj
            and its id and uses it to store the obj instance dictionary in
            the private class attribute '__objects')

            Args:
                obj (dict) : An instance object.
        '''
        objNameId = obj.__class__.__name__ + "." + obj.id
        type(self).__objects[objNameId] = obj

    def save(self):
        """
        Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """

        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            dict_storage = {}
            for key, val in type(self).__objects.items():
                dict_storage[key] = val.to_dict()
            json.dump(dict_storage, file)


    def reload(self):
        """Deserializes the Json file to objects if it exists"""
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                objdict = json.load(file)

                # Explanation - get the classname from each
                # entry to the json file
                # then use it to get the obj class e.g BaseModel
                # from the classes list
                # in model __init__ file and initialize the
                # object with the **kwargs
                for obj in objdict.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
                
                for key, val in type(self).__objects.items():
                    class_name = val['__class__']
                    del val["__class__"]
                    type(self).__objects[key] = eval(class_name)(**val)

        except FileNotFoundError:
            pass

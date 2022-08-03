#!/usr/bin/python3
'''
    Define class FileStorage
'''

import json
import models

class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
            Return the dictionary
        '''
        return self.__objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id

            (Basically this function gets the cls name of the passed obj 
            and its id and uses it to store the obj instance dictionary in
            the private class attribute '__objects')
            
            Args:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    
    def save(self):
        """
        Write the JSON serialization of a list of objects to a file.
        
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        
        filename = FileStorage.__file_path

        obj_dict = {}

        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value

        with open(filename, mode="w", encoding="UTF-8") as jsonfile:
            json.dump(obj_dict, jsonfile)


    def reload(self):

        filename = FileStorage.__file_path
        try:
            with open(filename, mode="r", encoding="UTF8") as jsonfile:
                FileStorage.__objects = json.load(jsonfile)

            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                FileStorage.__objects[key] = class_name(**val)

        except FileNotFoundError:
            pass

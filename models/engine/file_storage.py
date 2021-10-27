#!/usr/bin/python3
'''This module defines the class FileStorage'''

from models.base_model import BaseModel

import os
import json


class FileStorage:
    '''Defining class FileStorage'''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''Returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets obj with obj class.id'''
        name = obj.__class__.__name__
        key = name + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        '''serializes __objects to the json file'''
        filename = self.__file_path
        jsonDic = {}
        with open(filename, 'w') as objsTOjson:
            for key, value in self.__objects.items():
                jsonDic[key] = value.to_dict()
            json.dump(jsonDic, objsTOjson)

    def reload(self):
        '''load objs from json file'''
        from models import ClassDic
        try:
            with open(self.__file_path, 'r') as jsonTOobjs:
                all_json = json.load(jsonTOobjs)
                for key in all_json:
                    obj = all_json[key]
                    self.__objects[key] = ClassDic[obj['__class__']](**obj)
        except:
            pass

#!/usr/bin/python3
'''This module is defining class BaseModel'''
import uuid
from datetime import datetime
import models


class BaseModel():
    '''Base model for future classes'''

    def __init__(self, *args, **kwargs):
        '''init method of BaseModel'''
        if kwargs:
            for key in kwargs:
                if key in ('created_at', 'updated_at'):
                    kwargs[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                if key != ('__class__'):
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''string representation of the BaseModel'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates update_at attribute with current date/time'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''return dictionary containing key:value from __dict__'''
        newDic = self.__dict__.copy()
        newDic['__class__'] = self.__class__.__name__
        newDic['created_at'] = self.created_at.isoformat()
        newDic['updated_at'] = self.updated_at.isoformat()

        return newDic

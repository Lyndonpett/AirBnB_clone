#!/usr/bin/python3
'''This module is defining class Amenity'''

from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Defining Amenity inherited from BaseModel'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not kwargs:
            self.name = ""

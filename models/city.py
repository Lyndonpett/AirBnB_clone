#!/usr/bin/python3
'''This module is defining class City'''

from models.base_model import BaseModel


class City(BaseModel):
    '''Defining City inherited from BaseModel'''

    def __init__(self, **kwargs):
        '''Init for City from BaseModel'''
        super().__init__(**kwargs)
        if not kwargs:
            self.name = ""
            self.state_id = ""

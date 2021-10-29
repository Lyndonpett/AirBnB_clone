#!/usr/bin/python3
'''This module defines class User from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Defining User, inherited from Basemodel'''

    def __init__(self, **kwargs):
        '''Init for User from BaseModel'''
        super().__init__(**kwargs)
        if not kwargs:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""

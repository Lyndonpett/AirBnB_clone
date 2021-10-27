#!/usr/bin/python3
'''This module is defining class City'''

from models.base_model import BaseModel


class City(BaseModel):
    '''Defining City inherited from BaseModel'''

    name = ""
    state_id = ""

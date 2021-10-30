#!/usr/bin/python3
'''This module defines class User from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''Defining User, inherited from Basemodel'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

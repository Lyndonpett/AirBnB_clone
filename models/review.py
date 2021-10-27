#!/usr/bin/python3
'''This modules defines class Review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Defining Review inherited from BaseModel'''

    place_id = ""
    user_id = ""
    text = ""

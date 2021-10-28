#!/usr/bin/python3
'''This module defines class State'''

from models.base_model import BaseModel


class State(BaseModel):
    '''Defining State inherited from BaseModel'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not kwargs:
            self.name = ""

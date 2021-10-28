#!/usr/bin/python3
'''This modules defines class Review'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''Defining Review inherited from BaseModel'''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not kwargs:
            self.place_id = ""
            self.user_id = ""
            self.text = ""

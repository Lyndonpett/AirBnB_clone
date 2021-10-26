#!/usr/bin/python3
'''Linking FileStorage to BaseModel'''

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

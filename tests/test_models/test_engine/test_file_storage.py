#!/usr/bin/python3
'''FileStorage Unittests'''

import models
from models.engine.file_storage import FileStorage
import unittest
import os
import json
import types


class TestFileStorage(unittest.TestCase):
    '''Tests for FileStorage class'''

    # setup testing objects
    FS = FileStorage()
    base = models.BaseModel(id='420',
                            created_at='1999-12-31T11:59:59.999999',
                            updated_at='1999-12-31T11:59:59.999999'
                            )

    def setUp(self):
        '''clear models.storage for each test'''
        if os.path.exists('file.json'):
            os.remove('file.json')
        # can't change the size of a dictionary while iterating through it
        junk = [obj for obj in models.storage.all()]
        for key in junk:
            models.storage.delete(key)

    def test_init(self):
        '''test the init method of FileStorge'''
        self.assertIsInstance(self.FS, FileStorage)

    def test_new(self):
        '''use new() to add obj to FileStorage obj'''
        self.assertIsInstance(self.FS.new, types.MethodType)
        models.storage.new(self.base)
        self.assertDictEqual(models.storage.all(),
                             {'BaseModel.420': self.base}
                             )
        with self.assertRaises(TypeError):
            self.FS.new()

    def test_all(self):
        '''confirm that all() returns the expected dictionary'''
        self.assertIsInstance(self.FS.all, types.MethodType)
        self.assertIsInstance(models.storage.all(), dict)
        self.assertDictEqual(models.storage.all(), {})
        models.storage.new(self.base)
        self.assertDictEqual(
            models.storage.all(), {'BaseModel.420': self.base})

    def test_save(self):
        '''test that save() writes the expected output in the expected file'''
        self.assertIsInstance(self.FS.save, types.MethodType)
        models.storage.new(self.base)
        models.storage.save()
        with open('file.json') as file:
            json_str = ['{"BaseModel.420": {"id": "420", "created_at":',
                        ' "1999-12-31T11:59:59.999999", "updated_at":',
                        ' "1999-12-31T11:59:59.999999", "__class__":',
                        ' "BaseModel"}}'
                        ]
            self.assertDictEqual(
                json.load(file), json.loads("".join(json_str)))

    def test_reload(self):
        '''confirm reload deserializes json strings into correct objects'''
        self.assertIsInstance(self.FS.reload, types.MethodType)
        models.storage.reload()
        self.assertEqual(models.storage.all(), {})
        models.storage.new(self.base)
        models.storage.save()
        models.storage.reload()
        self.assertDictEqual(
            models.storage.all()['BaseModel.420'].to_dict(),
            self.base.to_dict()
        )

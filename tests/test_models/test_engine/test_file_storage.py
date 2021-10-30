#!/usr/bin/python3
'''FileStorage Unittests'''

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''FileStorage tests'''

    def setUp(self):
        '''setup before each test'''
        self.FS = FileStorage()

    def tearDown(self):
        '''remove file.json at end of test'''
        if os.path.exists('file.json'):
            os.remove('file.json')
# test __str__

    def test_new(self):
        with self.assertRaises(TypeError):
            self.FS.new()

    def test_all(self):
        '''tests self.all()'''
        thing = BaseModel(id='420',
                          created_at='1999-12-31T11:59:59.999999',
                          updated_at='1999-12-31T11:59:59.999999'
                          )
        self.FS.new(thing)
        self.assertDictEqual(self.FS.all(), {'BaseModel.420': thing})

    def test_save(self):
        '''tests self.save()'''
        thing = BaseModel(id='420',
                          created_at='1999-12-31T11:59:59.999999',
                          updated_at='1999-12-31T11:59:59.999999'
                          )
        self.FS.new(thing)
        self.FS.save()
        with open('file.json') as file:
            json_str = ['{"BaseModel.420": {"id": "420", "created_at":',
                        ' "1999-12-31T11:59:59.999999", "updated_at":',
                        ' "1999-12-31T11:59:59.999999", "__class__":',
                        ' "BaseModel"}}'
                        ]
            self.assertDictEqual(
                json.load(file), json.loads("".join(json_str)))

    def test_reload(self):
        """tests the reload method"""
        self.FS.reload()
        self.assertEqual(self.FS.all(), {})
        thing = BaseModel(id='420', created_at='1999-12-31T11:59:59.999999',
                          updated_at='1999-12-31T11:59:59.999999')
        self.FS.new(thing)
        self.FS.save()
        self.FS.reload()
        self.assertEqual(str(self.FS.all().get("BaseModel.420")), str(thing))

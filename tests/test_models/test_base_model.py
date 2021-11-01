#!/usr/bin/python3
'''Base Model Unittests'''

import models
from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class TestBase(unittest.TestCase):
    '''Tests for BaseModel class'''

    # setup testing objects
    kwargs = {'updated_at': '1999-12-31T11:59:59.999999',
              'created_at': '1999-12-31T11:59:59.999999',
              'id': '420',
              '__class__': 'BaseModel'}
    base = BaseModel()
    base2 = BaseModel(**kwargs)

    def setUp(self):
        '''clear models.storage for each test'''
        if os.path.exists('file.json'):
            os.remove('file.json')
        # can't change the size of a dictionary while iterating through it
        junk = [obj for obj in models.storage.all()]
        for key in junk:
            models.storage.delete(key)

    def test_init(self):
        '''Create BaseModel and confirm value types'''
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsInstance(self.base.id, str)
        self.base.id = 2
        self.assertEqual(2, self.base.id)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.to_dict(), dict)

    def test_init_kwargs(self):
        '''Create BaseModel using **kwargs'''
        self.assertIsInstance(self.base2, BaseModel)
        self.assertEqual(self.base2.id, "420")
        self.assertIsInstance(self.base2.updated_at, datetime.datetime)
        self.assertIsInstance(self.base2.created_at, datetime.datetime)
        self.assertIsInstance(self.base2.to_dict(), dict)
        self.assertDictEqual(self.base2.to_dict(), self.kwargs)

    def test__str__(self):
        '''Confirm BaseModel.__str__ returns correctly'''
        self.assertEqual(str(self.base), self.base.__str__())
        self.assertEqual(str(self.base), "[BaseModel] ({}) {}".
                         format(self.base.id, self.base.__dict__))
        self.assertEqual(str(self.base2), "[BaseModel] ({}) {}".
                         format(self.base2.id, self.base2.__dict__))

    def test_to_dict(self):
        '''Confirm the BaseModel.to_dict() returns correctly'''
        base3 = BaseModel(**self.kwargs)
        self.assertDictEqual(self.kwargs, base3.to_dict())

    def test_save(self):
        '''Run BaseModel.save() and confirm file contents'''
        oldUpdate = self.base2.updated_at
        self.base2.save()
        self.assertNotEqual(self.base2.created_at, self.base2.updated_at)
        self.assertNotEqual(oldUpdate, self.base2.updated_at)
        with open('file.json', 'r') as file:
            self.assertDictEqual(
                json.load(file), {'BaseModel.420': self.base2.to_dict()})


if __name__ == '__main__':
    unittest.main()

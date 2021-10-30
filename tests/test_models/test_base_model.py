#!/usr/bin/python3
'''Base Model Unittests'''

import unittest
import datetime
from models.base_model import BaseModel
import json


class TestBase(unittest.TestCase):
    '''Tests for BaseModels class'''

    def testBase(self):
        '''Tests values after creating BaseModel'''

        base = BaseModel()
        self.assertIsInstance(base.id, str)
        base.id = 2
        self.assertIsInstance(base, BaseModel)
        self.assertEqual(2, base.id)
        self.assertIsInstance(base.updated_at, datetime.datetime)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.to_dict(), dict)

    def testKwargs(self):
        '''Tests base created with dict'''

        testDic = {"updated_at": "2021-10-29T23:26:48.287044",
                   "created_at": "2021-10-29T23:26:48.287044",
                   "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9",
                   "__class__": "BaseModel"}
        base2 = BaseModel(**testDic)
        self.assertIsInstance(base2, BaseModel)
        self.assertEqual(base2.id, "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9")
        self.assertIsInstance(base2.updated_at, datetime.datetime)
        self.assertIsInstance(base2.created_at, datetime.datetime)
        self.assertIsInstance(base2.to_dict(), dict)

    def testBaseSave(self):
        '''Tests base save'''

        base3 = BaseModel()
        oldUpdate = base3.updated_at
        base3.save()
        self.assertNotEqual(base3.created_at, base3.updated_at)
        self.assertNotEqual(oldUpdate, base3.updated_at)

    def testToDict(self):
        '''Tests todict '''
        c = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263",
                      updated_at="1020-02-13T07:10:03.134263",
                      __class__="test123")
        cDict = c.to_dict()
        s = ["{'id': 69, 'created_at': ",
             "'1000-07-29T12:14:07.132263', ",
             "'updated_at': '1020-02-13T07:10:03.134263',",
             " '__class__': 'BaseModel'}"]
        stringline = s[0] + s[1] + s[2] + s[3]
        self.assertEqual(str(cDict), stringline, "dict not match in toDict()")
        self.assertIsInstance(cDict["updated_at"], str,
                              "updated_at not ISO string. used in toDict()")
        self.assertIsInstance(cDict["created_at"], str,
                              "created_at not ISO string. used in toDict()")

    def testSTR(self):
        '''Tests base __str__'''
        b = BaseModel()
        self.assertEqual(str(b), "[BaseModel] ({}) {}".
                         format(b.id, b.__dict__))

    def testSave(self):
        '''another chance for save?'''
        c = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263",
                      updated_at="1020-02-13T07:10:03.134263",
                      __class__="test123")
        lastUpdate = str(c.updated_at)
        c.save()
        self.assertNotEqual(str(c.updated_at),
                            lastUpdate,
                            "updated_at did not change when using save()")

    def testpassClass(self):
        '''documentation'''
        c = BaseModel(id=69, created_at="1000-07-29T12:14:07.132263",
                      updated_at="1020-02-13T07:10:03.134263",
                      __class__="test123")
        self.assertEqual(c.__class__, BaseModel,
                         "class is assigned as attribute in __init__")


if __name__ == '__main__':
    unittest.main()

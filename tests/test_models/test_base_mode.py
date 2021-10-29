#!/usr/bin/python3
'''Base Model Unittests'''

import unittest
import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    '''Tests for BaseModels class'''

    def testBase(self):
        '''Tests values after creating BaseModel'''

        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.id, str)

    def testKwargs(self):
        '''Tests base created with dict'''

        testDic = {"updated_at": "2021-10-29T23:26:48.287044", "created_at": "2021-10-29T23:26:48.287044",
                   "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9", "__class__": "BaseModel"}
        base2 = BaseModel(**testDic)
        self.assertIsInstance(base2, BaseModel)
        self.assertEqual(base2.id, "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9")
        self.assertIsInstance(base2.updated_at, datetime.datetime)
        self.assertIsInstance(base2.created_at, datetime.datetime)
        self.assertIsInstance(base2.to_dict(), dict)

    def testBaseSave(self):
        '''Tests base save'''

        base3 = BaseModel()
        base3.save()
        self.assertNotEqual(base3.created_at, base3.updated_at)

    def testTo_Dict(self):
        '''Tests base to_dict'''

        testDic = {"updated_at": "2021-10-29T23:26:48.287044", "created_at": "2021-10-29T23:26:48.287044",
                   "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9", "__class__": "BaseModel"}
        obj2 = BaseModel(**testDic)

        obj = BaseModel(**testDic)
        objDict = obj2.to_dict()
        self.assertDictEqual(obj2.__dict__, obj.__dict__)
        self.assertEqual(objDict["id"], "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9")
        self.assertEqual(objDict["created_at"], "2021-10-29T23:26:48.287044")
        self.assertEqual(objDict["updated_at"], "2021-10-29T23:26:48.287044")
        self.assertIsInstance(objDict["id"], str)
        self.assertIsInstance(objDict["created_at"], str)
        self.assertIsInstance(objDict["updated_at"], str)

    def testSTR(self):
        '''Tests base __str__'''

        testDic = {"updated_at": "2021-10-29T23:26:48.287044", "created_at": "2021-10-29T23:26:48.287044",
                   "id": "5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9", "__class__": "BaseModel"}
        obj = BaseModel(**testDic)

        testStr = obj.__str__()
        self.assertEqual(
            testStr[:52], "[BaseModel] (5b9de3e3-1c3e-47ee-8ed0-98bb95eaa2a9) {")
        self.assertEqual(testStr[-1:], "}")

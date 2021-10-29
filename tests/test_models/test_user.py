#!/usr/bin/python3
'''Unittests for User class'''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''Tests for User Class'''

    def setUp(self):
        '''sets User to U variable'''

        self.u = User()

    def testInit(self):
        self.assertEqual(self.u.email, "")
        self.assertEqual(self.u.password, "")
        self.assertEqual(self.u.first_name, "")
        self.assertEqual(self.u.last_name, "")

        Dic = self.u.to_dict()
        ob = User(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.u is ob)


if __name__ == '__main__':
    unittest.main()

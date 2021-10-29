#!/usr/bin/python3
'''Unittests for class City'''


import unittest
from models.city import City


class testCity(unittest.TestCase):
    '''Tests for class City'''

    def setUp(self):
        '''Setting city() to city variable'''

        self.city = City()

    def testInit(self):
        '''testing city class'''

        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

        Dic = self.city.to_dict()
        ob = City(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.city is ob)


if __name__ == '__main__':
    unittest.main()

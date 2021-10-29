#!/usr/bin/python3
'''Unittests for class Amenity'''


import unittest
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    '''Tests for class Amenity'''

    def setUp(self):
        '''Setting Amenity() to Amenity variable'''

        self.amenity = Amenity()

    def testInit(self):
        '''testing Amenity class'''

        self.assertEqual(self.amenity.name, "")

        Dic = self.amenity.to_dict()
        ob = Amenity(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.amenity is ob)


if __name__ == '__main__':
    unittest.main()

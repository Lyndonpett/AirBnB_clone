#!/usr/bin/python3
'''Unittests for class Place'''


import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    '''Tests for class Place'''

    def setUp(self):
        '''Setting Place() to place variable'''

        self.place = Place()

    def testInit(self):
        '''testing place class'''

        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

        Dic = self.place.to_dict()
        ob = Place(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.place is ob)


if __name__ == '__main__':
    unittest.main()

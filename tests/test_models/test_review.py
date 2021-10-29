#!/usr/bin/python3
'''Unittests for class Review'''


import unittest
from models.review import Review


class testReview(unittest.TestCase):
    '''Tests for class Review'''

    def setUp(self):
        '''Setting Review() to Review variable'''

        self.review = Review()

    def testInit(self):
        '''testing Review class'''

        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

        Dic = self.review.to_dict()
        ob = Review(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.review is ob)


if __name__ == '__main__':
    unittest.main()

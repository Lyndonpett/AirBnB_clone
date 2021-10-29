#!/usr/bin/python3
'''Unittests for class State'''


import unittest
from models.state import State


class testState(unittest.TestCase):
    '''Tests for class State'''

    def setUp(self):
        '''Setting State() to state variable'''

        self.state = State()

    def testInit(self):
        '''testing state class'''

        self.assertEqual(self.state.name, "")

        Dic = self.state.to_dict()
        ob = State(**Dic)
        self.assertEqual(ob.to_dict(), Dic)
        self.assertFalse(self.state is ob)


if __name__ == '__main__':
    unittest.main()

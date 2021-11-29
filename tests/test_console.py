#!/usr/bin/python3
'''Console Unittests'''
import unittest
import console
import os
import types
import models
import sys
from io import StringIO


class TestColsole(unittest.TestCase):
    '''Test console methods'''

    con = console.HBNBCommand()
    true_out = sys.stdout

    def setUp(self):
        '''clear models.storage for each test'''
        if os.path.exists('file.json'):
            os.remove('file.json')
        # can't change the size of a dictionary while iterating through it
        junk = [obj for obj in models.storage.all()]
        for key in junk:
            models.storage.delete(key)
        # establish new stream every test instead of truncating the same one
        # used to capture prints from console methods
        self.out = StringIO()
        sys.stdout = self.out

    def tearDown(self):
        '''breakdown after each test'''
        sys.stdout = self.true_out

    def test_instance(self):
        '''Confirm console type and properties'''
        self.assertIsInstance(self.con, console.HBNBCommand)
        self.assertEqual(self.con.prompt, '(hbnb) ')
        self.assertIsInstance(self.con.do_quit, types.MethodType)
        self.assertIsInstance(self.con.do_EOF, types.MethodType)
        self.assertIsInstance(self.con.emptyline, types.MethodType)
        self.assertIsInstance(self.con.do_create, types.MethodType)
        self.assertIsInstance(self.con.do_show, types.MethodType)
        self.assertIsInstance(self.con.do_destroy, types.MethodType)
        self.assertIsInstance(self.con.do_all, types.MethodType)
        self.assertIsInstance(self.con.do_update, types.MethodType)
        self.assertIsInstance(self.con.default, types.MethodType)

    def test_Console_Exit(self):
        '''Confirm console ends as expected'''
        with self.assertRaises(SystemExit):
            self.con.do_quit()
            self.con.do_EOF()

    def test_emptyline(self):
        '''Confirm emptyline does nothing'''
        self.con.emptyline()
        self.assertEqual(self.out.getvalue(), '')
        self.con.do_all(None)
        self.assertEqual(self.out.getvalue(), '[]\n')

    def test_Amenity_ais(self):
        '''Confirm creation of Amenity class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('Amenity')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('Amenity')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('Amenity ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('Amenity ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_BaseModel_adis(self):
        '''Confirm creation of BaseModel class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('BaseModel')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('BaseModel')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('BaseModel ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('BaseModel ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_City_ais(self):
        '''Confirm creation of City class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('City')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('City')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('City ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('City ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_Place_ais(self):
        '''Confirm creation of Place class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('Place')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('Place')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('Place ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('Place ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_Review_ais(self):
        '''Confirm creation of Review class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('Review')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('Review')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('Review ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('Review ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_State_ais(self):
        '''Confirm creation of State class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('State')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('State')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('State ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('State ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')

    def test_User_ais(self):
        '''Confirm creation of User class
        tests init/all/show/destroy methods
        '''
        self.con.do_create('User')
        out2 = StringIO()
        sys.stdout = out2
        self.con.do_all('User')
        out3 = StringIO()
        sys.stdout = out3
        self.con.do_show('User ' + self.out.getvalue()[:-1])
        self.assertEqual(out2.getvalue()[2:-3], out3.getvalue()[:-1])
        out4 = StringIO()
        sys.stdout = out4
        self.con.do_destroy('User ' + self.out.getvalue()[:-1])
        self.con.do_all(None)
        self.assertEqual(out4.getvalue(), '[]\n')


# update & default nice!

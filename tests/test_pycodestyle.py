#!/usr/bin/python3
'''Pycodestyle Unittests'''
import unittest
import pycodestyle
import os


class TestPycodestyle(unittest.TestCase):
    '''Tests files for requirements'''

    files = ('models/engine/file_storage.py',
             'models/amenity.py',
             'models/base_model.py',
             'models/city.py',
             'models/place.py',
             'models/review.py',
             'models/state.py',
             'models/user.py',
             'console.py'
             )

    def test_pycodestyle(self):
        '''run pycodestyle against all .py files in app'''
        self.assertEqual(pycodestyle.StyleGuide(
            quiet=True).check_files('.').total_errors, 0)

    def test_shabang(self):
        '''open all files and confirm the first line is a shabang'''
        for item in self.files:
            with open(item) as f:
                self.assertEqual(f.readline(), "#!/usr/bin/python3\n",
                                 "First line needs shebang in {}".format(item))

    def test_readme(self):
        '''checks for non-empty README'''
        with open("README.md") as f:
            self.assertNotEqual(len(f.read()), 0, "README is empty")
        with open("tests/README.md") as f:
            self.assertNotEqual(len(f.read()), 0, "tests/README is empty")

    def test_exe(self):
        '''confirm all files are executable'''
        for item in self.files:
            self.assertTrue(os.access(item, os.X_OK),
                            "File {} is not executable".format(item))

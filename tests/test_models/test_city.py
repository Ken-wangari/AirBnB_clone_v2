#!/usr/bin/python3
"""Test module for City class"""

import os
import unittest
import pycodestyle
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test case for the City class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """Tear down after the test"""
        del cls.city

    def tearDown(self):
        """Tear down after each test method"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_conformance(self):
        """Test PEP8 conformance"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_docstrings(self):
        """Test for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes(self):
        """Test City attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass(self):
        """Test if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_types(self):
        """Test attribute types for City"""
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.state_id, str)

    def test_save_method(self):
        """Test the save method"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()


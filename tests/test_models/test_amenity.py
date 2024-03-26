#!/usr/bin/python3
"""A unit test for Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_inheritance(self):
        """
        Test if Amenity class inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """
        Test initialization of attributes in Amenity class.
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_str_method(self):
        """
        Test the __str__() method of Amenity class.
        """
        amenity = Amenity()
        expected_string = "[Amenity] ({}) {}".format(amenity.id,
                                                     amenity.__dict__)
        self.assertEqual(str(amenity), expected_string)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of Amenity class.
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')


if __name__ == '__main__':
    unittest.main()

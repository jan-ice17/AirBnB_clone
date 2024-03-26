#!/usr/bin/python3
"""A unittest file for City"""

import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_inheritance(self):
        """
        Test if City class inherits from BaseModel.
        """
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """
        Test initialization of attributes in City class.
        """
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_method(self):
        """
        Test the __str__() method of City class.
        """
        city = City()
        expected_string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(str(city), expected_string)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of City class.
        """
        city = City()
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')

    def test_attribute_assignment(self):
        """
        Test attribute assignment in City class.
        """
        city = City()
        city.state_id = "test_state_id"
        city.name = "test_name"
        self.assertEqual(city.state_id, "test_state_id")
        self.assertEqual(city.name, "test_name")


if __name__ == '__main__':
    unittest.main()

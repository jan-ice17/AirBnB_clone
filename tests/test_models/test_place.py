#!/usr/bin/python3
"""A unittest file for Review"""


import unittest
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_inheritance(self):
        """
        Test if Place class inherits from BaseModel.
        """
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """
        Test initialization of attributes in Place class.
        """
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str_method(self):
        """
        Test the __str__() method of Place class.
        """
        place = Place()
        expected_string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(str(place), expected_string)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of Place class.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_attribute_assignment(self):
        """
        Test attribute assignment in Place class.
        """
        place = Place()
        place.city_id = "test_city_id"
        place.user_id = "test_user_id"
        place.name = "test_name"
        place.description = "test_description"
        place.number_rooms = 5
        place.number_bathrooms = 2
        place.max_guest = 8
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["amenity1", "amenity2"]
        self.assertEqual(place.city_id, "test_city_id")
        self.assertEqual(place.user_id, "test_user_id")
        self.assertEqual(place.name, "test_name")
        self.assertEqual(place.description, "test_description")
        self.assertEqual(place.number_rooms, 5)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 8)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])


if __name__ == '__main__':
    unittest.main()

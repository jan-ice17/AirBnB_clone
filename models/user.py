#!/usr/bin/python3
"""A class User that inherits from BaseModel."""

import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Testing use cases for the User class.
    """

    def test_inheritance(self):
        """
        Testing  if User class inherits from BaseModel.
        """
        user = User()
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """
        Tests initialization of attributes in User class.
        """
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str_method(self):
        """
        Test the __str__() method of User class.
        """
        user = User()
        expected_string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_string)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of User class.
        """
        user = User()
        user_dict = user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')

    def test_attribute_assignment(self):
        """
        Tests attribute assignment in User class.
        """
        user = User()
        user.email = "test_email"
        user.password = "test_password"
        user.first_name = "test_first_name"
        user.last_name = "test_last_name"
        self.assertEqual(user.email, "test_email")
        self.assertEqual(user.password, "test_password")
        self.assertEqual(user.first_name, "test_first_name")
        self.assertEqual(user.last_name, "test_last_name")


if __name__ == '__main__':
    unittest.main()

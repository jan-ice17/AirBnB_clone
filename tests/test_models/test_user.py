#!/usr/bin/python3
"""A unittest file for User"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Testing for the User class."""

    def test_initialization(self):
        """Test initialization of User."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()

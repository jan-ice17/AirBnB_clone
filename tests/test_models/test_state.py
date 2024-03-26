#!/usr/bin/python3
"""A unittest file for state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Testing for the state class."""
    def test_initialization(self):
        """Test initialization of State."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()

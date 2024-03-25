import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Testing for the City class."""

    def test_initialization(self):
        """Test initialization of City."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()





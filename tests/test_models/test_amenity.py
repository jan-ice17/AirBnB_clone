import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_initialization(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()

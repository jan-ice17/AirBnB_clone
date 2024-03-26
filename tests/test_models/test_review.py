#!/usr/bin/python3
"""A unittest file for Review"""

import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    Tests cases for the Review class.
    """

    def test_inheritance(self):
        """
        Testing if Review class inherits from BaseModel.
        """
        review = Review()
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """
        Testing if initialization of attributes in Review class.
        """
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_method(self):
        """
        Test the __str__() method of Review class.
        """
        review = Review()
        expected_string = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_string)

    def test_to_dict_method(self):
        """
        Test the to_dict() method of Review class.
        """
        review = Review()
        review_dict = review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')

    def test_attribute_assignment(self):
        """
        Test attribute assignment in Review class.
        """
        review = Review()
        review.place_id = "test_place_id"
        review.user_id = "test_user_id"
        review.text = "test_text"
        self.assertEqual(review.place_id, "test_place_id")
        self.assertEqual(review.user_id, "test_user_id")
        self.assertEqual(review.text, "test_text")


if __name__ == '__main__':
    unittest.main()

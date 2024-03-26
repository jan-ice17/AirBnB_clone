#!usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Testing if BaseModel instances are initialized correctly."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Testing if the string rep of BaseModel instances is correct."""
        model = BaseModel()
        expected_output = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_output)

    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """Testing if unique IDs are generated for BaseModel instances."""
        self.assertTrue(isinstance(self.base_model.id, str))
        self.assertTrue(uuid.UUID(self.base_model.id))

    def test_created_at(self):
        """Testing if the 'created_at' attribute is of type datetime."""
        self.assertTrue(isinstance(self.base_model.created_at, datetime))

    def test_updated_at(self):
        """Testing if the 'updated_at' attribute is of type datetime."""
        self.assertTrue(isinstance(self.base_model.updated_at, datetime))

    def test_save_method(self):
        """Testing if the 'save' method updates the 'updated_at' attribute."""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Testing if the 'to_dict' converts instances to dict correctly."""
        base_model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertIn('id', base_model_dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_from_dict(self):
        """Testing if BaseModel instances can be instantiated
        from dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, model.id)
        self.assertEqual(new_model.created_at, model.created_at)
        self.assertEqual(new_model.updated_at, model.updated_at)

    def setUp(self):
        """Set up a dictionary for testing 'from_dict' method."""
        self.base_model_dict = {
            'id': 'test_id',
            'created_at': '2022-01-01T12:00:00.000000',
            'updated_at': '2022-01-01T12:00:00.000000',
            '__class__': 'BaseModel',
            'extra_attribute': 'extra_value'
        }

    def tearDown(self):
        """Clean up after testing."""
        del self.base_model


if __name__ == '__main__':
    unittest.main()

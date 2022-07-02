#!/usr/bin/python3
"""
    Tests for class City
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """testing City"""

    def test_docs(self):
        """check docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_city(self):
        """testing City with ok parameters"""
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertIsInstance(my_city, BaseModel)
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertIsInstance(my_city.state_id, str)
        self.assertTrue(hasattr(my_city, "name"))
        self.assertEqual(type(my_city.name), str)
        self.assertTrue(hasattr(my_city, "created_at"))
        self.assertTrue(hasattr(my_city, "updated_at"))
        self.assertTrue(hasattr(my_city, "id"))

    def test_str(self):
        """testing str method"""
        my_city = City()
        city_str = f'[{City.__name__}] ({my_city.id}) {my_city.__dict__}'
        self.assertEqual(city_str, str(my_city))

    def test_save(self):
        """test save method"""
        my_city = City()
        my_city.save()
        self.assertNotEqual(my_city.created_at, my_city.updated_at)

    def test_to_dict(self):
        """test to_dict methos"""
        my_city = City()
        my_dict = my_city.to_dict()
        self.assertEqual(type(my_dict), dict)


if __name__ == '__main__':
    unittest.main()

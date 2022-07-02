#!/usr/bin/python3
"""
    Tests for class City
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing Place"""

    def test_docs(self):
        """check docstring"""
        self.assertIsNotNone(Place.__doc__)

    def test_place(self):
        """testing class Place and it's attributes"""
        my_place = Place()
        self.assertIsInstance(my_place, Place)
        self.assertIsInstance(my_place, BaseModel)
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertEqual(type(my_place.city_id), str)
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertEqual(type(my_place.user_id), str)
        self.assertTrue(hasattr(my_place, "name"))
        self.assertEqual(type(my_place.name), str)
        self.assertTrue(hasattr(my_place, "description"))
        self.assertEqual(type(my_place.description), str)
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertEqual(type(my_place.number_rooms), int)
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertEqual(type(my_place.number_bathrooms), int)
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertEqual(type(my_place.max_guest), int)
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertEqual(type(my_place.price_by_night), int)
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertEqual(type(my_place.latitude), float)
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertEqual(type(my_place.longitude), float)
        self.assertTrue(hasattr(my_place, "amenity_ids"))
        self.assertEqual(type(my_place.amenity_ids), list)
        self.assertTrue(hasattr(my_place, "created_at"))
        self.assertTrue(hasattr(my_place, "updated_at"))
        self.assertTrue(hasattr(my_place, "id"))

    def test_str(self):
        """testing str method for class Place"""
        my_place = Place()
        place_str = f'[{Place.__name__}] ({my_place.id}) {my_place.__dict__}'
        self.assertEqual(place_str, str(my_place))

    def test_save(self):
        """test save method for class Place"""
        my_place = Place()
        my_place.save()
        self.assertNotEqual(my_place.created_at, my_place.updated_at)

    def test_to_dict(self):
        """test to_dict method for class Place"""
        my_place = Place()
        my_dict = my_place.to_dict()
        self.assertEqual(type(my_dict), dict)


if __name__ == '__main__':
    unittest.main()

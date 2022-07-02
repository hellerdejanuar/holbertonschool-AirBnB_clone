#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_amenity_class(self):
        """ test for class and instance """
        obj_am = Amenity()

        self.assertEqual(obj_am.__class__, Amenity)

    def test_amenity_id(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'id'), True)
        self.assertEqual(type(obj_am.id), str)

    def test_amenity_created_at(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'created_at'), True)
        self.assertEqual(type(obj_am.created_at), datetime)

    def test_amenity_updated_at(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'updated_at'), True)
        self.assertEqual(type(obj_am.updated_at), datetime)

    def test_amenity_name(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(hasattr(obj_am, 'name'), True)
        self.assertEqual(type(obj_am.name), str)

    def test_amenity_dict(self):
        """ test correct attributes of the class """
        obj_am = Amenity()

        self.assertTrue(type(obj_am.to_dict()), dict)

    def test_amenity_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_am = Amenity()
        obj_am_d = obj_am.to_dict()

        self.assertEqual(obj_am_d["__class__"], "Amenity")
        self.assertEqual(type(obj_am_d["id"]), str)
        self.assertEqual(type(obj_am_d["created_at"]), str)
        self.assertEqual(type(obj_am_d["updated_at"]), str)
        self.assertTrue(type(obj_am_d), dict)
        self.assertNotEqual(obj_am_d, obj_am.__dict__)

    def test_ids(self):
        """ test differente objects ids """
        obj_am_1 = Amenity()
        obj_am_2 = Amenity()

        self.assertEqual(type(obj_am_1), type(obj_am_2))
        self.assertNotEqual(obj_am_1.id, obj_am_2.id)

        id_2 = obj_am_2.id

        obj_am_2.id = '1234'

        self.assertEqual(obj_am_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = Amenity()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "Amenity")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_am_3 = Amenity()
        str_obj_3 = str(obj_am_3)
        str_compare = '[{}] ({}) <{}>'.format(
                type(obj_am_3).__name__, obj_am_3.id, obj_am_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_am_5 = Amenity()

        created_at_1 = obj_am_5.created_at
        updated_at_1 = obj_am_5.updated_at

        obj_am_5.save()

        created_at_2 = obj_am_5.created_at
        updated_at_2 = obj_am_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_am_6 = Amenity()
        self.assertIn(obj_am_6, models.storage.all().values())

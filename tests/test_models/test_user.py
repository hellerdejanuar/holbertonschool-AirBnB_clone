#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_user_class(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertEqual(obj_ur.__class__, User)

    def test_user_id(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'id'), True)
        self.assertEqual(type(obj_ur.id), str)

    def test_user_created_at(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'created_at'), True)
        self.assertEqual(type(obj_ur.created_at), datetime)

    def test_user_updated_at(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'updated_at'), True)
        self.assertEqual(type(obj_ur.updated_at), datetime)

    def test_user_email(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'email'), True)
        self.assertEqual(type(obj_ur.email), str)

    def test_user_password(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'password'), True)
        self.assertEqual(type(obj_ur.password), str)

    def test_user_first_name(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'first_name'), True)
        self.assertEqual(type(obj_ur.first_name), str)

    def test_user_last_name(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(hasattr(obj_ur, 'last_name'), True)
        self.assertEqual(type(obj_ur.last_name), str)

    def test_user_dict(self):
        """ test correct atributes of the class """
        obj_ur = User()

        self.assertTrue(type(obj_ur.to_dict()), dict)

    def test_user_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_ur = User()
        obj_ur_d = obj_ur.to_dict()

        self.assertEqual(obj_ur_d["__class__"], "User")
        self.assertEqual(type(obj_ur_d["id"]), str)
        self.assertEqual(type(obj_ur_d["created_at"]), str)
        self.assertEqual(type(obj_ur_d["updated_at"]), str)
        self.assertTrue(type(obj_ur_d), dict)
        self.assertNotEqual(obj_ur_d, obj_ur.__dict__)

    def test_ids(self):
        """ test differente objects ids """
        obj_ur_1 = User()
        obj_ur_2 = User()

        self.assertEqual(type(obj_ur_1), type(obj_ur_2))
        self.assertNotEqual(obj_ur_1.id, obj_ur_2.id)

        id_2 = obj_ur_2.id

        obj_ur_2.id = '1234'

        self.assertEqual(obj_ur_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = User()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "User")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_ur_3 = User()
        str_obj_3 = str(obj_ur_3)
        str_compare = '[{}] ({}) <{}>'.format(
                type(obj_ur_3).__name__, obj_ur_3.id, obj_ur_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_ur_5 = User()

        created_at_1 = obj_ur_5.created_at
        updated_at_1 = obj_ur_5.updated_at

        obj_ur_5.save()

        created_at_2 = obj_ur_5.created_at
        updated_at_2 = obj_ur_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_ur_6 = User()
        self.assertIn(obj_ur_6, models.storage.all().values())

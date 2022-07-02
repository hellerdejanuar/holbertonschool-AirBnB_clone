#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.review import Review
import models
from datetime import datetime


class TestAirbnb(unittest.TestCase):
    def test_review_class(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertEqual(obj_re.__class__, Review)

    def test_review_id(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'id'), True)
        self.assertEqual(type(obj_re.id), str)

    def test_review_created_at(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'created_at'), True)
        self.assertEqual(type(obj_re.created_at), datetime)

    def test_review_updated_at(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'updated_at'), True)
        self.assertEqual(type(obj_re.updated_at), datetime)

    def test_review_place_id(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'place_id'), True)
        self.assertEqual(type(obj_re.place_id), str)

    def test_review_user_id(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'user_id'), True)
        self.assertEqual(type(obj_re.user_id), str)

    def test_review_text(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(hasattr(obj_re, 'text'), True)
        self.assertEqual(type(obj_re.text), str)

    def test_review_dict(self):
        """ test correct atributes of the class """
        obj_re = Review()

        self.assertTrue(type(obj_re.to_dict()), dict)

    def test_review_to_dict(self):
        """ test the objet in dictionary representation like method to_dict """
        obj_re = Review()
        obj_re_d = obj_re.to_dict()

        self.assertEqual(obj_re_d["__class__"], "Review")
        self.assertEqual(type(obj_re_d["id"]), str)
        self.assertEqual(type(obj_re_d["created_at"]), str)
        self.assertEqual(type(obj_re_d["updated_at"]), str)
        self.assertTrue(type(obj_re_d), dict)
        self.assertNotEqual(obj_re_d, obj_re.__dict__)

    def test_ids(self):
        """ test differente objects ids """
        obj_re_1 = Review()
        obj_re_2 = Review()

        self.assertEqual(type(obj_re_1), type(obj_re_2))
        self.assertNotEqual(obj_re_1.id, obj_re_2.id)

        id_2 = obj_re_2.id

        obj_re_2.id = '1234'

        self.assertEqual(obj_re_2.id, '1234')

    def test_to_dict(self):
        """Test to_dict() method of BaseClass """
        model = Review()
        model.name = "My First Model"
        model.my_number = 89
        model_dict = model.to_dict()
        keys = ["id", "name", "my_number", "created_at",
                "updated_at", "__class__"]
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertIn("my_number", model_dict)
        self.assertIn("name", model_dict)
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "Review")
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)

    def test_str(self):
        """ test the string representation of the object """
        obj_re_3 = Review()
        str_obj_3 = str(obj_re_3)
        str_compare = '[{}] ({}) {}'.format(
                type(obj_re_3).__name__, obj_re_3.id, obj_re_3.__dict__)

        self.assertEqual(str_obj_3, str_compare)

    def test_doc(self):
        """Docstring"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)

    def test_save(self):
        """ test save method`"""
        obj_re_5 = Review()

        created_at_1 = obj_re_5.created_at
        updated_at_1 = obj_re_5.updated_at

        obj_re_5.save()

        created_at_2 = obj_re_5.created_at
        updated_at_2 = obj_re_5.updated_at

        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_stored(self):
        """ test correct storage """
        obj_re_6 = Review()
        self.assertIn(obj_re_6, models.storage.all().values())

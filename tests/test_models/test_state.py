#!/usr/bin/python3
"""
    Tests for class State
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """testing State"""

    def test_docs(self):
        """check docstring"""
        self.assertIsNotNone(State.__doc__)

    def test_state(self):
        """testing State with ok parameters"""
        my_state = State()
        self.assertIsInstance(my_state, State)
        self.assertIsInstance(my_state, BaseModel)
        self.assertTrue(hasattr(my_state, "name"))
        self.assertEqual(type(my_state.name), str)
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))
        self.assertTrue(hasattr(my_state, "id"))

    def test_str(self):
        """testing str method"""
        my_state = State()
        state_str = f'[{State.__name__}] ({my_state.id}) {my_state.__dict__}'
        self.assertEqual(state_str, str(my_state))

    def test_save(self):
        """test save method"""
        my_state = State()
        my_state.save()
        self.assertNotEqual(my_state.created_at, my_state.updated_at)

    def test_to_dict(self):
        """test to_dict methos"""
        my_state = State()
        my_dict = my_state.to_dict()
        self.assertEqual(type(my_dict), dict)


if __name__ == '__main__':
    unittest.main()

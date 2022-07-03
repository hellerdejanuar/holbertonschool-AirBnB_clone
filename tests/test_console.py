#!/usr/bin/python3
"""
Tests for the command interpreter
"""
import unittest
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def test_prompt(self):
        """test for the correct prompt"""
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_quit(self):
        """test when receiving 'quit' command"""
        pass

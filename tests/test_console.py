#!/usr/bin/python3
"""
Tests for the command interpreter
"""
import unittest
from console import HBNBCommand
import unittest
import pycodestyle
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os


class TestConsole(unittest.TestCase):

    def test_prompt(self):
        """
        test for the correct prompt
        """
        self.assertEqual('(hbnb) ', HBNBCommand.prompt)

    def test_quit(self):
        """
        test when receiving 'quit' command
        """
        pass

    def test_do_quit(self):
        """
        Test do_quit method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("quit")
            self.assertEqual(input_t.getvalue(), "")

    def test_EOF(self):
        """
        Test do_EOF method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(input_t.getvalue(), "")

    def test_emptyline(self):
        """
        test emptyline method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("\n")
            self.assertEqual(input_t.getvalue(), "")

    def test_do_create(self):
        """
        test do_create method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create Amenityzcv")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")

    def test_do_show(self):
        """
        test do_show method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show Usertre")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show User 9")
            self.assertEqual(input_t.getvalue(), "** no instance found **\n")

    def test_do_destroy(self):
        """
        test do_destroy
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy Everything")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy User 9")
            self.assertEqual(input_t.getvalue(), "** no instance found **\n")

    def test_do_all(self):
        """
        test do_all method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("all Userfdsf")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")

    def test_do_update(self):
        """
        test de_update method
        """
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update Userdasd")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as inpt:
            HBNBCommand().onecmd("update User 9")
            self.assertEqual(inpt.getvalue(), "** attribute name missing **\n")

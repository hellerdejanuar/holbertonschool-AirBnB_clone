#!/usr/bin/python3
"""
Console: contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex  # split based on lexical expressions
import sys


class HBNBCommand(cmd.Cmd):
    """
    Class Cmd, the imported implements quit/EOF, help, and a custom prompt
    """
    # prompt = '(hbnb) '
    if sys.stdin and sys.stdin.isatty():
        prompt = '(hbnb) '
    else:
        prompt = '(hbnb)\n'

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ End of file reached, exit """
        return True

    def emptyline(self):
        """ Empty """
        pass

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id
        Attributes:
            obj_key: "classname.id"
        """
        if args:
            argv = shlex.split(args)
            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            else:
                obj_key = argv[0] + '.' + argv[1]
                if obj_key in storage.all().keys():
                    print(storage.all()[obj_key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        Attributes:
            inst: new instance class to be created
        """
        if args:
            if args in storage.classes():
                inst = storage.classes()[args]()
                inst.save()
                print(inst.id)

            elif args not in storage.classes():
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Attributes:
            obj_key: "classname.id"
        """
        if args:
            argv = shlex.split(args)
            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            else:
                obj_key = argv[0] + '.' + argv[1]
                if obj_key in storage.all().keys():
                    del storage.all()[obj_key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        Attributes:
            obj_key: "classname.id"
            obj: object with name obj_key
            attr_type: type of argv[2] (str, int, float, list, datetime)
            str_list: list of strings to be list object
        """
        if args:
            argv = shlex.split(args)
            if len(argv) >= 2:
                obj_key = argv[0] + '.' + argv[1]

            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                print("** attribute name missing **")
            elif obj_key not in storage.all().keys():
                print("** no instance found **")
            elif len(argv) == 3:
                print("** value missing **")
            else:
                # Handling of args as data
                obj = storage.all()[obj_key]
                attr_type = type(getattr(obj, argv[2]))

                # Handles args as integers
                if attr_type == int:
                    setattr(obj, argv[2], int(argv[3]))
                # Floats
                elif attr_type == float:
                    setattr(obj, argv[2], float(argv[3]))
                # List of strings
                elif attr_type == list:
                    str_list = argv[3].strip('][').split(', ')
                    setattr(obj, argv[2], str_list)
                    # convert string repr of list "[1, 2, 3]" into list obj
                # Strings
                elif attr_type == str:
                    setattr(obj, argv[2], argv[3])
                else:
                    print("unknown type")
                storage.save()
        else:
            print("** class name missing **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        Attributes:
            obj_list: empty list that will contain all objects stored
        """
        obj_list = []

        if not args:
            for obj_key in storage.all():
                obj_list.append(str(storage.all()[obj_key]))
            print(obj_list)
        else:
            argv = shlex.split(args)
            if argv[0] in storage.classes():
                for obj_key in storage.all():
                    if storage.all()[obj_key].__class__.__name__ == argv[0]:
                        obj_list.append(str(storage.all()[obj_key]))
                print(obj_list)
            else:
                print("** class doesn't exist **")

    def precmd(self, args):
        """
        Process command before
        Attribute:
            input_cmd[0]: class name of args
            input_cmd[1]: requested function
        """
        if not args:
            return cmd.Cmd.precmd(self, args)

        args_list = shlex.split(args)
        if args_list[0][-2:] != '()':
            return cmd.Cmd.precmd(self, args)
        else:
            try:
                input_cmd = args_list[0].split('.')
                input_cmd[1] = input_cmd[1][:-2]
                if input_cmd[0] in storage.classes().keys():
                    if input_cmd[1] in self.functions():
                        command_line = input_cmd[1] + ' ' + input_cmd[0]
                        return cmd.Cmd.precmd(self, f'\
                                {input_cmd[1]} {input_cmd[0]}')
                        # handle extra arguments
            except Exception:
                pass

        return cmd.Cmd.precmd(self, args)

    @staticmethod
    def functions():
        """
        Returns a dict of functions
        """
        func_list = [
                'all',
                'show',
                'create',
                'destroy',
                'update'
                ]
        return func_list


if __name__ == '__main__':
    HBNBCommand().cmdloop()

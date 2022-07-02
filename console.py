#!/usr/bin/python3
""" Console """
import cmd
import json
from models import storage
from models.base_model import BaseModel
import shlex

class HBNBCommand(cmd.Cmd):
    """ Class Cmd """
    prompt = '(hbnb) '

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
        """ Prints the string representation of an instance
        based on the class name and id """
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
        """ Creates a new instance of BaseModel """
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
        """ Deletes an instance based on the class name and id """
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
        """  Updates an instance based on the class name and id
        by adding or updating attribute """
        if args:
            argv = shlex.split(args)

            if argv[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(argv) == 1:
                print("** instance id missing **")
            elif len(argv) == 2:
                print("** attribute name missing **")
            elif len(argv) == 3:
                print("** value missing **")
            else:
                obj_key = argv[0] + '.' + argv[1]

                if obj_key in storage.all().keys():
                    obj = storage.all()[obj_key]
                    attr_type = type(getattr(obj, argv[2]))

                    if attr_type == int:
                        setattr(obj, argv[2], int(argv[3]))
                    elif attr_type == float:
                        setattr(obj, argv[2], float(argv[3]))
                    elif attr_type == list:
                        str_list = argv[3].strip('][').split(', ')
                        setattr(obj, argv[2], str_list)
                        # convert string repr of list "[1, 2, 3]" into list obj
                    elif attr_type == str:
                        setattr(obj, argv[2], argv[3])
                    else:
                        print("unknown type")
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")



    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name """
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

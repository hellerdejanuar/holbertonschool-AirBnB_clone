#!/usr/bin/python3
""" Console """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Class Cmd """
    prompt = '(hbnb)'

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
            argv = args.split()
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


    def do_update(self, args):
        """  Updates an instance based on the class name and id
        by adding or updating attribute """

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name """
        obj_list = []

        for obj in storage.all():
            obj_list.append(str(storage.all()[obj]))
        print(obj_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

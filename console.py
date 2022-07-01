#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, args):
        """ End of file reached, exit """
        return True

    def emptyline(self):
        pass

    def do_show(self, args):
        """ Prints the string representation of an instance 
        based on the class name and id """

    def do_create(self, args):
        """ """

    def do_destroy(self, args):
        """ """
    
    def do_update(self, args):
        """ """

if __name__ == '__main__':
    HBNBCommand().cmdloop()

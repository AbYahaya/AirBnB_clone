#!/usr/bin/python3
""""
This is the consoleof the AirBnB_clone project,

It was created by Yahaya Abdulrauf:
    2/11/2024
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, args):
        """
        Type 'exit' to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        EOF to exit the console
        """
        return True

    def emptyline(self):
        """
        Ensures the console does nothing if emptyline is ENTERED
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

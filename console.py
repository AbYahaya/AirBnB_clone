#!/usr/bin/python3
""""
This is the consoleof the AirBnB_clone project,

It was created by Yahaya Abdulrauf:
    2/11/2024
"""
import cmd
import models
import importlib
from models.base_model import BaseModel


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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        entered_line = args.split()
        if not self.entered_line.verify_cls(entered_line):
            return
        class_name = entered_line[0]

        try:
            module = importlib.import_module(class_name)
            instance = getattr(module, class_name)

            if isinstance(instance, BaseModel):
                instance.save()
                print(instance.id)
            return
        except:
            pass

        def do_show(self, args):
            """
            Prints the string representation of an instance based on the
            class name and id
            """
            entered_line = args.split()

            if not self.entered_line.verify_cls(entered_line):
                return
            if not self.entered_line.verify_id(entered_line):
                return

            key = '{}.{}'.format(entered_line[0],entered_line[1])
            str_rep = models.storage.all()
            print(str_rep[key])

        @classmethod
        def verify_cls(cls, entered_line):
            """
            A class mehtod to verify that entered line is in the class_list
            """
            if len(entered_line) == 0:
                print("** class name missing **")
                return False
            elif entered_line[0] not in HBNB.class_list:
                print("** class doesn't exist **")
                return False
            return True

        @staticmethod
        def verify_id(entered_line):
            """
            Static method to verify the id
            """
            if len(entered_line) < 2:
                print("** instance id missing **")
                return False
            str_rep = models.storage.all()

            key = '{}.{}'.format(entered_line[0], entered_line[1])
            if key not in str_rep.key():
                print("** no instance found **")
                return False
            return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

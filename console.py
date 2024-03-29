#!/usr/bin/python3
""""
This is the consoleof the AirBnB_clone project,

It was created by Yahaya Abdulrauf:
    2/11/2024
'str_rep' holds all objects returned by all()
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    class_list = ['BaseModel', 'User', 'Place', 'City', 'State',
                  'Review']

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
        if not self.verify_cls(entered_line):
            return
        instance = eval(entered_line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        entered_line = args.split()

        if not self.verify_cls(entered_line):
            return
        if not self.verify_id(entered_line):
            return

        key = '{}.{}'.format(entered_line[0], entered_line[1])
        str_rep = models.storage.all()
        print(str_rep[key])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        entered_line = args.split()

        if not self.verify_cls(entered_line):
            return
        if not self.verify_id(entered_line):
            return
        key = '{}.{}'.format(entered_line[0], entered_line[1])
        str_rep = models.stroage.all()
        del str_rep[key]
        models.storage.all()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        entered_line = args.split()
        str_rep = models.storage.all()
        to_be_printed = []
        if len(entered_line) == 0:
            for value in str_rep.values():
                to_be_printed.append(str(value))
                print(to_be_printed)
        elif entered_line[0] in HBNBCommand.class_list:
            for k, v in str_rep.items():
                if entered_line[0] in k:
                    to_be_printed.append(str(v))
                    print(to_be_printed)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
         Updates an instance based on the class name and id by adding
         or updating attribute (save the change into the JSON file
        """
        entered_line = args.split()
        if not self.verify_cls(entered_line):
            return
        if not self.verify_id(entered_line):
            return
        if not self.verify_attr(entered_line):
            return
        str_rep = models.storage.all()
        key = '{}.{}'.format(entered_line[0], entered_line[1])
        setattr(str_rep[key], entered_line[2], entered_line[3])
        models.storage.save()

    def default(self, args):
        """
        Method called when an argument is passed to determine what class
        to work on
        """
        entered_line = args.strip('()').split('.')
        if len(entered_line) < 2:
            print("** No attribute **")
            return
        str_rep = models.storage.all()
        class_name = entered_line[0].capitalize()
        split1 = entered_line[1].strip(')').split('(').lower()
        cmd_name = split1[0]
        if cmd_name == 'all':
            HBNBCommand.do_all(self, class_name)
        elif cmd_name == 'show':
            if len(split1) < 2:
                print("** instance id missing **")
            else:
                HBNBCommand.do_show(self, class_name + ' ' + split1[1])
        elif cmd_name == 'update':
            split2 = split1[1].split(',')

            if len(split2) == 0:
                print("** No instance **")
            elif len(split2) == 1 and type(split2[1]) == dict:
                for key, value in split2[1].items():
                    HBNBCommand.do_update(self, class_name + ' '
                                          + split2[1] + ' ' + key + ' '
                                          + value)
            elif len(split2) == 1 and type(split2[1]) != dict:
                print("** no instance found **")
            elif len(split2) == 2:
                print("** no instance found **")
            else:
                HBNBCommand.do_update(self, class_name + ' ' + split2[0] +
                                      ' ' + split2[1] + ' ' + split2[2])
        elif cmd_name == 'destroy':
            if len(split1) < 2:
                print("** no instance **")
            else:
                HBNBCommand.do_destroy(self, class_name + ' ' + split1[1])
        elif cmd_name == 'count':
            count = 0
            for k in objects.keys():
                key = k.split('.')
                if class_name == key[0]:
                    count += 1
            print(count)

    @classmethod
    def verify_cls(cls, entered_line):
        """
        A class method to verify that entered line is in the class_list
        """
        if len(entered_line) == 0:
            print("** class name missing **")
            return False
        elif entered_line[0] not in HBNBCommand.class_list:
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
        if key not in str_rep.keys():
            print("** no instance found **")
            return False
        return True

    @staticmethod
    def verify_attr(entered_line):
        """
        To veriry if entered_line has attributed and values
        """

        if len(entered_line) < 3:
            print("** attribute name missing **")
            return False
        if len(entered_line) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

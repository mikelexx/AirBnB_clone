#!/usr/bin/python3
"""
Console entry point
"""

from shlex import split
from ast import parse
from models.base_model import BaseModel
import cmd
import sys
from models.user import User
from models import storage
import re

def parsee(arg):
    """Parses aruments passed"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """A class that defines a console"""
    prompt = '(hbnb) '
    __myclasses = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """a command to quit the terminal"""
        sys.exit()

    def do_EOF(self, arg):
        """a command to quit the terminal"""
        sys.exit()

    # def do_hbnb(self, arg):
    #     """custom command to implment hbnb"""
    #     print("excuiting hbnb")

    def emptyline(self):
        """pass an empty input"""
        pass

    def do_create(self, arg):
        """
        Usage : create <classname>
        Create a Class with console"""
        argl = parsee(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__myclasses:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Usage : show <classnames> <id>
        Prints the string representation of an instance"""
        argl = parsee(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__myclasses:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Usage: destroy <classname> <id>
        destroys a class
        """
        argl = parsee(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__myclasses:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Usage: all <classname>
        list all objects of a class
        """
        argl = parsee(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__myclasses:
            print("** class doesn't exist **")
        else:
            mylist = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    mylist.append(obj.__str__())
                elif len(argl) == 0:
                    mylist.append(obj.__str__())
            print(mylist)

    def do_update(self, arg):
        """
        Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance"""
        argl = parsee(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__myclasses:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    """Entry point"""
    HBNBCommand().cmdloop()
    cmd.cmdloop()

#!/usr/bin/env python3
"""
this module contains the entry point of the command interpreter
"""
import cmd
import sys
import re
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ creaters a simple command line interface"""
    if sys.stdin.isatty():
        prompt = "(hbnb) "
    else:
        prompt = "(hbnb)\n"
    bnb_models = [
            "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    class_name_objects = r"\w+\.all\(\)"
    class_name_objects_count = r"\w+\.count\(\)"
    class_name_obj_id_show = r"\w+\.show\(\"[\w-]+\"\)"
    tmp_regex = r"\w+\.update\(\"[\w+-]+\", {'[\w+': \",]+}\)"
    class_name_obj_id_update = tmp_regex
    class_name_obj_id_destroy = r"\w+\.destroy\(\"[\w-]+\"\)"

    def do_create(self, line):
        """
        Creates a new instance of arbnb model, saves it (to the JSON file
         ) and prints the id. Ex: $ create BaseModel
         Args:
            line: str: input from the terminal or stdin.
        """
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in self.bnb_models:
            print("** class doesn't exist **")
            return
        new_model = eval(args[0])()
        new_model.save()
        print(new_model.id)

    def do_update(self, line):
        """
         Updates an instance based on the class name and id by adding or
         updating attribute (
         save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
         Args:
            line: input from the console.
         """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.bnb_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            input_id = args[0] + "." + args[1]
            loaded_objects_dictionary = models.storage.all()
            for key, val in loaded_objects_dictionary.items():
                if key == input_id:
                    if len(args) < 3:
                        print("** attribute name missing **")
                        return
                    if len(args) < 4:
                        print("** value missing **")
                        return
                    if args[2] in val.__dict__:
                        if args[3].isdigit():
                            setattr(val, args[2], int(args[3]))
                        else:
                            setattr(val, args[2], args[3])
                        models.storage.save()
                        return
            return

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.
        Args:
            line: (str) line containing class name and id
                e.g Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.bnb_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        input_id = args[0] + "." + args[1]
        loaded_objects_dictionary = models.storage.all()
        for key, val in loaded_objects_dictionary.items():
            if key == input_id:
                print(loaded_objects_dictionary[key])
                return
        print("** no instance found **")
        return

    def do_destroy(self, line):
        """
         Deletes an instance based on the class name and id (
         save the change into the JSON file).
         Example: $ destroy BaseModel 1234-1234-1234.
         Args:
         line : input from console
         """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.bnb_models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        input_id = args[0] + "." + args[1]
        loaded_objects_dictionary = models.storage.all()
        for key, val in loaded_objects_dictionary.items():
            if key == input_id:
                del loaded_objects_dictionary[key]
                models.storage.save()
                return
        print("** no instance found **")
        return

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not
        on the class name.
        Ex: $ all BaseModel or $ all.
        Args:
            line: cmd prompt argument
        """
        args = line.split()
        loaded_objects_dictionary = models.storage.all()
        if len(args) == 0:
            for key, val in loaded_objects_dictionary.items():
                print(val)
            return
        elif args[0] in self.bnb_models:
            for key, val in loaded_objects_dictionary.items():
                if val.__class__.__name__ == args[0]:
                    print(val)
            return
        else:
            print("** class doesn't exist **")
            return

    def show_class_objects(self, input_class_name):
        """
        prints all instances of a class by using: <class name>.all().
        Args:
            input_class_name: cmd prompt input of form- <class name>.all().
        """
        result = []
        loaded_objects_dictionary = models.storage.all()
        for key, val in loaded_objects_dictionary.items():
            if val.__class__.__name__ == input_class_name:
                result.append(val)
        print("[", end="")
        for val in result[:-1]:
            print(val, end="")
            print(", ", end="")
        if len(result) > 0:
            print(result[-1], end="")
        print("]")

    def show_class_count(self, input_class_name):
        """
        prints the number of instances of a class: <class name>.count().
        Args:
            input_class_name: prompt input of form: <class name>.count().
        """
        loaded_objects_dictionary = models.storage.all()
        count = 0
        for key, val in loaded_objects_dictionary.items():
            if val.__class__.__name__ == input_class_name:
                count += 1
        print(count)

    def default(self, line):
        """
        For manipulating objects starting with class_name
        and id or class name only in input
        Args:
            line: inputs from command prompt
        """
        input_class_name = line.split(".")[0]
        if re.match(self.class_name_objects, line):
            self.show_class_objects(input_class_name)
        elif re.match(self.class_name_objects_count, line):
            self.show_class_count(input_class_name)
        elif re.match(self.class_name_obj_id_show, line):
            obj_id = line.split("(\"")[1].split("\")")[0]
            self.do_show(' '.join([input_class_name, obj_id]))
        elif re.match(self.class_name_obj_id_update, line):
            pattern = r"\w+\.update\(\"([\w+-]+)\", {('[\w+': \",]+)}\)"
            obj_id = re.search(pattern, line).group(1)
            attributes = re.search(pattern, line).group(2).replace("'", "\"")
            attributes_dict = json.loads("{" + attributes + "}")
            for key, val in attributes_dict.items():
                update_args = [input_class_name, obj_id, key, str(val)]
                update_args = ' '.join(update_args)
                self.do_update(update_args)
        elif re.match(self.class_name_obj_id_destroy, line):
            obj_id = line.split("(\"")[1].split("\")")[0]
            self.do_destroy(' '.join([input_class_name, obj_id]))
        else:
            print("*** Unknown syntax: {:s}".format(line))

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """
        gives a clean way of exit from interpreter.
        Args:
            line type(str): end of file command e.ge. CNTRL +d.
        Returns: True so as to exit interpreter.
        """
        print()
        return True

    def emptyline(self):
        """ prevents invoking last command if empty line is entered"""
        pass

    def do_help(self, line):
        cmd.Cmd.do_help(self, line)
        if len(line) > 0 and sys.stdin.isatty():
            print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

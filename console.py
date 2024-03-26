#!usr/bin/python3

import cmd
import shlex
import sys
import models
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Interactive command-line interface for managing models."""

    prompt = '(hbnb) '

    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def do_quit(self, argument):
        """Exit the command-line interface."""
        return True

    def do_EOF(self, argument):
        """Exit the command-line interface."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, argument):
        """Create a new instance of a model."""
        if argument:
            if argument in self.classes:
                get_class = getattr(sys.modules[__name__], argument)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, argument):
        """Display the string representation of an instance."""
        tokens = shlex.split(argument)
        if len(tokens) == 0:
            print("** class name missing **")
        elif len(tokens) == 1:
            print("** instance id missing **")
        elif tokens[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            keyU = tokens[0] + '.' + str(tokens[1])
            if keyU in dic:
                print(dic[keyU])
            else:
                print("** no instance found **")

    def do_destroy(self, argument):
        """Delete an instance based on the class name and id."""
        tokensD = shlex.split(argument)
        if len(tokensD) == 0:
            print("** class name missing **")
        elif len(tokensD) == 1:
            print("** instance id missing **")
        elif tokensD[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            key = tokensD[0] + '.' + tokensD[1]
            if key in dic:
                del dic[key]
                models.storage

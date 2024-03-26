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
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, argument):
        """Display all instances or instances of a specific class."""
        tokensA = shlex.split(argument)
        listI = []
        dic = models.storage.all()
        if len(tokensA) == 0:
            for key in dic:
                representation_Class = str(dic[key])
                listI.append(representation_Class)
            print(listI)
        elif tokensA[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            representation_Class = ""
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    representation_Class = str(dic[key])
                    listI.append(representation_Class)
            print(listI)

    def do_update(self, argument):
        """Update an instance based on the class name and id."""
        tokensU = shlex.split(argument)
        if len(tokensU) < 4:
            print("** arguments missing **")
            return
        if tokensU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass
        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()

    def do_count(self, argument):
        """Retrieve the number of instances of a class."""
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        for key in dic:
            className = key.split('.')
            if className[0] == tokensA[0]:
                num_instances += 1
        print(num_instances)

    def precmd(self, argument):
        """Execute just before the command line is interpreted."""
        args = argument.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return argument


if __name__ == '__main__':
    """Start the interactive command-line interface."""

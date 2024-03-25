#1/usr/bin/python3
"""Unit Test for the console"""
import unittest
from unittest.mock import patch
import io
import sys
import os
from console import HBNBCommand
from io import StringIO
from unittest.mock import create_autospec


class test_console(unittest.TestCase):
    """This is a test for the console module"""
    def set_up(self):
        """test for setup"""
        self.backup = sys.stdout
        self.get_output = StringIO()
        sys.stdout = self.get_output
    def setUp2(self):
        """Set up the HBNBCommand instance."""
        self.console = HBNBCommand()

    def test_prompt(self):
        """Test the prompt setup."""
        self.assertEqual('(hbnb) ', self.console.prompt)
 
    def test_quit(self):
        """Test the Quit command"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def tear_Down(self):
        """Test tear down"""
        sys.stdout = self.backup
    
    def create(self):
        """This create an instance of the HBNBCommand"""
        return HBNBCommand

    
    def test_EOF(self):
        """This Checks for the end of a file (EOF)"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))
    
    def test_all(self):
        """Test all command"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.get_output.getvalue(), str))
    
    def test_toshow_class_name(self):
        """Checking of class name is missing"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.get_output.getvalue()
        sys.stdout = self.backup
        self.get_output.close()
        self.get_output = StringIO()
        sys.stdout = self.get_output
        console.onecmd("show")
        x = (self.get_output.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_toshow_class_name2(self):
        """Checking if class name is not present"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.get_output.getvalue()
        sys.stdout = self.backup
        self.get_output.close()
        self.get_output = StringIO()
        sys.stdout = self.get_output
        console.onecmd("show User")
        x = (self.get_output.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    def test_instance_found(self):
        """Check if id is present"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.get_output.getvalue()
        sys.stdout = self.backup
        self.get_output.close()
        self.get_output = StringIO()
        sys.stdout = self.get_output
        console.onecmd("show User " + "124356876")
        x = (self.get_output.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """Create test"""
        console = self.create()
        console.onecmd("create User")
        self.assertTrue(isinstance(self.get_output.getvalue(), str)) 
        
        """Check if all show exist"""
        console = self.create()
        console.onecmd("create User")
        user_id = self.get_output.getvalue()
        sys.stdout = self.backup
        self.get_output.close()
        self.get_output = StringIO()
        sys.stdout = self.get_output
        console.onecmd("show User " + user_id)
        x = (self.get_output.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))
    
    def test_class_name(self):
        """Test to check if class name is missing"""
        console = self.create()
        console.onecmd("create")
        x = (self.get_output.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_if_a_class_name_exist(self):
        """Check if class name exist"""
        console = self.create()
        console.onecmd("create Menor")
        x = (self.get_output.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

if __name__ == '__main__':
    unittest.main()      


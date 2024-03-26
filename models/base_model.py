#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    A class(BaseModel) that defines all the common
    metthods or attributees for the other classes.
    Attributes:
        id (str): Generates a Unique id for each instance.
        created_at (datetime): Timestamp when an instance is created.
        updated_at (datetime): Timestamp of the last update to an instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        Args:
            *args: Variable length argument list (unused).
            **kwargs: Arbitrary keyword arguments to
            handle dictionary representation.
        """
        if kwargs:  # If kwargs is not empty
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)  # Set attribute name and value
            # Convert string datetime attributes to datetime objects
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:  # If kwargs is empty
            self.id = str(uuid.uuid4())  # Generate unique id
            self.created_at = datetime.now()  # Set created_at timestamp
            self.updated_at = datetime.now()  # Set updated_at timestamp
            models.storage.new(self)

    def __str__(self):
        """
        Provides a repr of the BaseModel in specific format.

        Returns:
            str: The string representation of the instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()  # Updates the last updated time.

    def new(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        THis will convert instance attributes to a dictionary.

        Returns:
            new_dictionary: A dictionary
            that contains all keys/values of the instances.
        """
        # This creates a copy of the instance's dictionary
        new_dict = self.__dict__.copy()
        # Convert datetime attributes to strings in ISO format.
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict  # Returns the modified dictionary.

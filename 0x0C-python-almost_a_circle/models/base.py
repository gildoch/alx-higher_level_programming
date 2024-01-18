#!/usr/bin/python3
"""
The ``base`` module
This ``base`` module supplies
"""
import json


class Base:
    """ A Sample of Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Base constructor method
        Args:
            id (int): id
        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Parameters:
        - list_dictionaries (list): A list of dictionaries.

        Returns:
        - str: JSON string representation of list_dictionaries.
        """
        # Ensure list_dictionary is a list
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Parameters:
        - cls (class): The class itself.
        - list_objs (list): A list of instances that inherit from Base.

        Returns:
        - None

        Raises:
        - TypeError: If list_objs is not a list.
        - ValueError: If any instance in the list does not inherit from Base.
        """
        filename = cls.__name__ + '.json'

        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
                f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string representation.

        Parameters:
        - json_string (str): A string representing a list of dictionaries
            in JSON format.

        Returns:
        - list: List represented by the JSON string.

        Raises:
        - TypeError: If json_string is not a string.
        - ValueError: If the JSON string is not valid or cannot be decoded.
        """
        if not json_string:
            return []

        return json.loads(json_string)

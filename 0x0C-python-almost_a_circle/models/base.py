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

        Raises:
        - TypeError: If list_dictionaries is not a list.
        - ValueError: If any dictionary in the list is not serializable to JSON
        """
        # Ensure list_dictionary is a list
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

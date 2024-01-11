#!/usr/bin/python3
"""
The ``base`` module
This ``base`` module supplies
"""


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

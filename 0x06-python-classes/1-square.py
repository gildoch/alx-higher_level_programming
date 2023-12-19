#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Defines a square
    Attributes:
        __size (int): size of a side of square
    """

    def __init__(self, size):
        """Intializes a square
        Args:
                size (int): size of a side of square
            Returns: None
        """
        self.__size = size

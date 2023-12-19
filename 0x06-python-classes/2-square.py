#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Defines a square
    Attributes:
        __size (int): size of a side of square
    """

    def __init__(self, size=0):
        """Intializes a square
        Args:
                size (int): size of a side of square
            Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

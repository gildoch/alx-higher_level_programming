#!/usr/bin/python3
"""
The ``10-square`` module
This ``10-square`` module provides one class Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ A Sample Square class """

    def __init__(self, size):
        """ Square constructor method
        Args:
            size (int): size of square
        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function that return the area of square
        Args:
            None
        Returns:
            area of square
        """
        return self.__size ** 2

    def __str__(self):
        """Return a square represantation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

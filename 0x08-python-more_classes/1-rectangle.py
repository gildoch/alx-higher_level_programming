#!/usr/bin/python3
""" Empty Definition of Rectangle Class"""


class Rectangle:
    """Definition of Rectangle"""

    def __init__(self, width=0, height=0):
        """Constructor method
        Args:
            width (int): The size of the rect width
            height (int: The size of the rect height

        Returns:
            None
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter method
        Return:
                width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method
        Args:
            value (int): The size of the rect width
        Return:
                None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height get method
        Return:
            Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method
        Args:
            value (int): The size of the rect height
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

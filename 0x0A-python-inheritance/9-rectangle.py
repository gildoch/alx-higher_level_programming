#!/usr/bin/python3
"""
The ``8-rectangle`` module
This ``8-rectangle`` module provides one class
Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Sample Rectangle class"""
    def __init__(self, width, height):
        """Rectangle constructor method
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        Returns:
            None
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Args:
            None
        Returns:
            area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the representation of a rectangle
        Args:
            None
        Returns:
            None
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

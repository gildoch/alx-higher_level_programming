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
        """Rectangle constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

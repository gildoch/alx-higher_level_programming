#!/usr/bin/python3
"""
The ``4-print_square`` module
This ``print_square`` module supplies one funtion, print_square(size):
"""


def print_square(size):
    """ Return a representation of a square
    Args:
        size (int): the size of the square
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)

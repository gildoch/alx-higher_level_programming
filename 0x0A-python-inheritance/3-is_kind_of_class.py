#!/usr/bin/python3
"""
The ```3-is_kind_of_class` module
This ``3-is_kind_of_class`` module provides one function,
3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """ Function that check the instance of a class
    Args:
        obj (obj): instance of a class
        a_class (class): class
    Returns:
        True if is an instance of the class
    """
    return isinstance(obj, a_class)

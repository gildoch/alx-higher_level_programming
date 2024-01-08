#!/usr/bin/python3
"""
The ``2-is_same_class`` module
This ``2-is_same_class`` module provides one function,
is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """ Function that check the instance of a class
    Args:
        obj (obj): instance of a class
        a_class (class): class
    Returns:
        True if is an instance of the class
    """
    return (type(obj) == a_class)

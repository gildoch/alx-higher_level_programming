#!/usr/bin/python3
"""
The ``4-inherits_from`` module
This ``4-inherits_from`` module provides one function,
def inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    otherwise False
    Args:
        obj (obj): instance of a class
        a_class (class): class
    Returns:
        True or False
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)

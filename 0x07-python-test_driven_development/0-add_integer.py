#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer.py supplies one function, add_integer(a, b)
"""


def add_integer(a, b=98):
    """Function to add 2 numbers and return the addition
    Args:
        a (int): first number
        b (int): second number
    Returns:
        addition
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

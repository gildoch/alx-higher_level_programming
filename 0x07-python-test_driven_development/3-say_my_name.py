#!/usr/bin/python3
"""
This is the "say_my_name" module
The "3-say_my_name" module supplies one function,
say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """Function that return a sentence with first name and last name
    Args:
        first_name (string): first name
        last_name (string): last name
    Returns:
        sentence
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

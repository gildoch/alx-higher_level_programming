#!/usr/bin/python3
"""Module that contains functions to write and append to a file"""


def append_write(filename="", text=""):
    """Function to write and append to a file
    Args:
        filename: filename

    Raises:
        Exception to opened file

    """

    with open(filename, "a", encoding='utf-8') as f:
        return f.write(text)

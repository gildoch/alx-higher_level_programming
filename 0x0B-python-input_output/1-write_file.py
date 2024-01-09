#!/usr/bin/python3
"""Module that contains functions to write to a file"""


def write_file(filename="", text=""):
    """Function to write to a file
    Args:
        filename: filename

    Raises:
        Exception to opened file

    """

    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)

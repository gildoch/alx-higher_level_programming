#!/usr/bin/python3
""" Module that contains a function to read from a file"""


def read_file(filename=""):
    """Function that Reads a text file

    Args:
        filename: filename

    Raises
        Exception when the file can be opened

    """

    with open(filename, mode='r', encoding='utf-8') as file:
        lines = file.read()
        print(lines, end="")

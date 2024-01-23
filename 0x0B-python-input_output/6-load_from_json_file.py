#!/usr/bin/python3
"""Module with functions to create an objects from JSON file"""
import json


def load_from_json_file(filename):
    """"Function that creates an Object from a JSON file
    Args:
        filename (file): filename path
    Raises:
        IO exceptions
    """
    with open(filename) as f:
        return json.loads(f.read())

#!/usr/bin/python3
"""Module with functions to save a object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """functions to save a object to a file

    Args:
        my_obj:object
        filename:filename

    Raises:
        Exception: When the object can't be serialized and file permission

    """

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)

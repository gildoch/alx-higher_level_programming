#!/usr/bin/python3
"""Module with function that return JSON representation of an object"""
import json


def to_json_string(my_obj):
    """function that return JSON representation of an object

    Args:
        my_object: object

    Raises:
        Exception: When the object can't be encoded

    """
    return json.dumps(my_obj)

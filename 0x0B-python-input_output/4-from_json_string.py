#!/usr/bin/python3
"""Module with function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON string

    Args:
        my_str:string
    Raises:
        Exception: when a object can't be loaded

    """
    return json.loads(my_str)

#!/usr/bin/python3
"""function that returns the dictionary description with simple data
structure"""
import json


def class_to_json(obj):
    """function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object:
    Args:
        obj (object) : object to serialize
    Raises:
        Exceptions
    """
    dict_desc = {}
    if hasattr(obj, '__dict__'):
        dict_desc = obj.__dict__.copy()
    return dict_desc

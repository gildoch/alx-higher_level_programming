#!/usr/bin/python3
"""Module with function that adds all arguments to a
Python list, and then save them to a file"""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args():
    """ arguments to a Python list, and then save them to a file
    Argss:
        None
    Raises:
        Exception:
    """
    filename = 'add_item.json'

    if len(sys.argv) > 1:
        if os.path.isfile(filename):
            old_data = load_from_json_file(filename)
        else:
            old_data = []

        old_data.extend(sys.argv[1:])
        save_to_json_file(old_data, filename)


def main():
    add_args()


main()

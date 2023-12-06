#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary))
    for f in keys:
        print("{}: {}".format(f, a_dictionary[f]))

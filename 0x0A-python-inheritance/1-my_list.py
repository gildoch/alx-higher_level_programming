#!/usr/bin/python3
"""A sample MyList class"""


class MyList(list):
    """Sub class of list object"""

    def __int__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))

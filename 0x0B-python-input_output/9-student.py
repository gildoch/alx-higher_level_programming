#!/usr/bin/python3
"""
Module containing Student class
"""


class Student():
    """
    Class representation of student
    """
    def __init__(self, first_name, last_name, age):
        """Student constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method to convert fields into dictionary"""
        return self.__dict__

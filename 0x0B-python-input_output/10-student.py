#!/usr/bin/python3
"""
Module containing Student class
"""


class Student:
    """
    Class representation of student
    """

    def __init__(self, first_name, last_name, age):
        """Student constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method to convert fields into dictionary"""
        dict_list = {}

        if type(attrs) is list:

            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__

                if attr in self.__dict__.keys():
                    dict_list[attr] = self.__dict__[attr]
        else:
            dict_list = self.__dict__.copy()

        return dict_list

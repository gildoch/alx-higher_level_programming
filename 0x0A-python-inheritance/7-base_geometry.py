#!/usr/bin/python3
"""
A Sample of BaseGeometry class
"""


class BaseGeometry:
    """Emppty  class """
    def area(self):
        """ Function that return the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

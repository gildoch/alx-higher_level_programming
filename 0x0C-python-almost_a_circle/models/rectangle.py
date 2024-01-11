#!/usr/bin/python3
"""
The ``rectangle`` module
This ``rectangle`` module provides one class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class, Base subclass """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle constructor method
        Args:
            width (int): width of the rectangle
            height (int): height od the rectangle
            x (int):
            y (int):
            id (int): id of object
        Returns:
            None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width getter
        Args:
            None
        Returns:
            width of rectangle
        """
        return self.__width

    @property
    def height(self):
        """ height getter
        Args:
            None
        Returns:
            height of rectangle
        """
        return self.__height

    @property
    def x(self):
        """ x getter
        Args:
            None
        Returns:
            value of x
        """
        return self.__x

    @property
    def y(self):
        """ y getter
        Args:
            None
        Returns:
            value of y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value (int): width of rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value (int): height of rectangle
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ x setter
        Args:
            value (int): value of x
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ y setter
        Args:
            value (int): value of y
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of rectangle
        Args:
            None
        Returns:
            area
        """
        return self.__width * self.__height

    def display(self):
        """ print a representation of a rectangle
        Args:
            None
        Returns:
            None
        """
        for z in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ return the representation of rectangle
        Args:
            None
        Returns:
            Custom message
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """ function to update the rectangle properties
        Args:
            args (list): list of args
        Returns:
            None
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

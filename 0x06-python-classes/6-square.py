#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """getter of __position
        Returns:
            The position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Returns:
            None
        """
        if (type(value) is not tuple) or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print square
        Return:
            None
        """
        if self.size > 0:
            for j in range(self.__position[1]):
                print()
            for x in range(self.size):
                print(' ' * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()

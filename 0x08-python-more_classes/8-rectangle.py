#!/usr/bin/python3
""" Empty Definition of Rectangle Class"""


class Rectangle:
    """Definition of Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor method
        Args:
            width (int): The size of the rect width
            height (int: The size of the rect height

        Returns:
            None
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter method
        Return:
                width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter method
        Args:
            value (int): The size of the rect width
        Return:
                None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height get method
        Return:
            Height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter method
        Args:
            value (int): The size of the rect height
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Function to calculate area of the rect
        Returns:
            Area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Function to calculate rectangle perimeter
        Returns:
            Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns printable string representation of the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """Create an object using representation string"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Delete instance message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Check if rectangles are equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

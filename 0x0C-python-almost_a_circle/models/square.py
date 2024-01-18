#!/usr/bin/python3
"""
Square class, subclass of Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A Sample square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ square constructor method
        Args:
            size (int): size of square
            x (int): padding x
            y (int): padding y
            id (int): id of square
        Retuns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return the square custom representation
        Args:
            None
        Returns:
            str
        """
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ size getter method
        Args:
            None
        Returns:
            size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter method
        Args:
            value (int): size of square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ function to update the attr
        Args:
            args (list): list of args
            kwargs (list): list of args
        Returns:
            None
        """

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

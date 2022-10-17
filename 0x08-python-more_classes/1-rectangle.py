#!/usr/bin/python3

""" The Rectangle Class Module """


class Rectangle:
    """for rectangle class
    """
    def __init__(self, width=0, height=0):
        """Constractor/initiliazer for Rectangle class

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter and setter for the width """
        return self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")

        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """ Getter and setter for the height """
        return self.__height

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")

        if val < 0:
            raise ValueError("height must be >= 0")

        self.__height = val

#!/usr/bin/python3

""" The Rectangle Class Module """


class Rectangle:
    """ Docs for rectangle class
    """
    def __init__(self, width=0, height=0):
        """Constractor/initiliazer for Rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter for the width """
        return self.__width

    @width.setter
    def width(self, val):
        """ Setter for the width field
        Args:
            val: value to be set the width
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")
        self.__width = val

    @property
    def height(self):
        """ Getter for the height """
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for the height field
        Args:
            val: new value of the height
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")

        if val < 0:
            raise ValueError("height must be >= 0")

        self.__height = val

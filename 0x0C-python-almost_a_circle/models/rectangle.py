#!/usr/bin/python3
""" Rectangle model module class """
from models.base import Base


class Rectangle(Base):
    """ the rectangle class that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor for the Rectangle class
        Args:
            width: with of the rectangle
            height: height of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width atrribute"""
        return self.__width

    @width.setter
    def width(self, val):
        """ setter for the width
        Args:
            val: new value
        """
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """getter for the height atrribute"""
        return self.__height

    @height.setter
    def height(self, val):
        """ setter for the height
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """getter for the x atrribute"""
        return self.__x

    @x.setter
    def x(self, val):
        """ setter for x
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """getter for the y atrribute"""
        return self.__y

    @y.setter
    def y(self, val):
        """ setter for y
        Args:
            val: new value
        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """ returns the area value of the Rectangle instance """
        return self.height * self.width

    def display(self):
        """ printible rep of the rectangle in # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for a in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for an in range(self.width)]
            print("")
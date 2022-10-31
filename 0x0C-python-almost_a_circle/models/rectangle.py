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
        if not isinstance(val, int):
            raise TypeError()
        if val < 0:
            raise ValueError()
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
            raise TypeError()
        if val < 0:
            raise ValueError()
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
            raise TypeError()
        if val < 0:
            raise ValueError()
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
            raise TypeError()
        if val < 0:
            raise ValueError()
        self.__y = val

#!/usr/bin/python3
""" Module for the Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from BaseGeometry"""
    def __init__(self, size):
        """ constructor for the Square class
        Args:
            width: width
            height: height
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

        self.__size = size

    def area(self):
        """ computes the area of Square """
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

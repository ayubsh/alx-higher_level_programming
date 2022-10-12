#!/usr/bin/python3

import sys

""" The square Class """


class Square:
    """ base class body of sqaure """

    def __init__(self, size=0):
        """ constructor for the square class
        Args:
            size: the size sqaure instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ compute the area of the current instance
        of square nad returns it
        """
        return self.__size * self.__size

    @property
    def size(self):
        """ size is getter that gets the private field__size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter that sets the private field __size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """ prints square using #"""
        if self.__size == 0:
            print("")
        for r in range(self.__size):
            for c in range(self.__size):
                print("{}".format("#"), end="", file=sys.stdout)
            print("")

#!/usr/bin/python3

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

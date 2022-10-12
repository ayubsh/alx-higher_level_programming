#!/usr/bi/python3

""" The square Class """


class Square:
    """ base class of square
    """
    def __init__(self, size=0):
        """ constructor method for the sqaure class
        Args:
            size: the size of the instance square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

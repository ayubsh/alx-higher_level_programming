#!/usr/bin/python3


""" The square Class """


class Square:
    """ base class body of sqaure """

    def __init__(self, size=0, position=(0, 0)):
        """ constructor for the square class
        Args:
            size: the size sqaure instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """ compute the area of the current instance
        of square nad returns it
        """
        return self.__size * self.__size

    @property
    def position(self):
        """ getter, gets the private field position"""
        return self.__position

    @property
    def size(self):
        """ size is getter that gets the private field__size
        """
        return self.__size

    @position.setter
    def position(self, value):
        """ Position setter to set the value of position"""
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

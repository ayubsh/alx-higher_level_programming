#!/usr/bin/python3
""" Base model Class """


class Base:
    """ The superclass where all other classes extends from
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for the base class
        Args:
            id: the id of the instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

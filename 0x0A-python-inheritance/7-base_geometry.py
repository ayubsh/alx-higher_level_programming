#!/usr/bin/python3
""" Module for the geometry class """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """ raises Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the name and value
        Args:
            name: name to be validated
            value: value to be validated
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

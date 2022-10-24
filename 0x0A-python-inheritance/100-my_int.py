#!/usr/bin/python3
""" Module Myint """


class MyInt(int):
    """ Myint class tha inherites from int class """
    def __eq__(self, this):
        """ change == behavior """
        return self.real != this

    def __ne__(self, this):
        """ change != behavior """
        return self.real == this

#!/usr/bin/python3
""" Mylist module """


class MyList(list):
    """ Mylist class that inherit from list class """
    def __init__(self):
        """" constructor for the Mylist class """
        super().__init__()

    def print_sorted(self):
        """ print sorted list in ascending """
        print(sorted(self))

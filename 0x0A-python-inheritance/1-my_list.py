#!/usr/bin/python3
""" Mylist module """


class MyList(list):
    """ Mylist class that inherit from list class """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ print sorted list in ascending """
        s = list(self)
        s.sort()
        print(s)

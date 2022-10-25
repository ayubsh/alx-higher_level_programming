#!/usr/bin/python3
""" Reading Files """


def read_file(filename=""):
    """ opens and reads file
    Args:
        filename: name of the file to be opened
    """
    with open(filename) as file:
        for line in file:
            print(line.rstrip())

#!/usr/bin/python3
"""Append to file """


def append_write(filename="", text=""):
    """ apppends to a file
    Args:
        filename: name of the file
        text: text to be written to the file
    Returns: returns number of character written
    """
    with open(filename, "a") as file:
        return file.write(text)

#!/usr/bin/python3
"""Write to file """


def write_file(filename="", text=""):
    """ writes to a file
    Args:
        filename: name of the file
        text: text to be written to the file
    Returns: returns number of character written
    """
    with open(filename, "a") as file:
        return file.write(text)

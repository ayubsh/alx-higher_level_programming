#!/usr/bin/python3
"""square function."""


def print_square(size):
    """ prints a square with the character #
    Args:
        size: is the size length of the square
    Raises:
        TypeError: if size is not int
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

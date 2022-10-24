#!/usr/bin/python3

""" Lookup module """


def lookup(obj):
    """ gets list of available attributes and methods
    Args:
        obj: is the instance object to get the attributes and methods it has
    """
    return list(dir(obj))

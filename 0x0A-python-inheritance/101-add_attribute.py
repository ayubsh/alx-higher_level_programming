#!/usr/bin/python3
""" module for add attributes """


def add_attribute(obj, n, v):
    """ add attributes to object if its possible
    Args:
        obj: object to add the attributes to
        n: name of the attributes
        v: value of the attributes
    Raises:
        TypeError: if obj can't be added attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, n, v)

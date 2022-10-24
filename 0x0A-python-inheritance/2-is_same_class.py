#!/usr/bin/python3
""" Same class module """


def is_same_class(obj, a_class):
    """ Checks weather obj is in the same class
        Args:
            obj: instance object
            a_class: class to be checked against
        Returns:
            True if the object is exactly an instance of the
            specified class otherwise False
    """

    if type(obj) == a_class:
        return True
    else:
        return False

#!/usr/bin/python3
""" Same class module """


def is_same_class(obj, a_class):
    """ Checks weather obj is in the same class
        Args:
            obj: instance object
            a_class: class to be checked against
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False

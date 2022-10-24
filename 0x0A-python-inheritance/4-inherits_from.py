#!/usr/bin/python3
""" module is kind of the same """


def inherits_from(obj, a_class):
    """Checks weather obj is intance of class or
        inherited class
        Args:
            obj: intance onject
            a_class: class to be checked against
        Returns:
            True if the object is instance if the
            specified class or inherited class otherwise
            False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

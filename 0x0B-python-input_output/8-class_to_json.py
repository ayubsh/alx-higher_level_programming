#!/usr/bin/python3
""" Class to json """


def class_to_json(obj):
    """ dictionaty description with simple data structure
    Args:
        obj: is an instance of a class
    """
    return obj.__dict__

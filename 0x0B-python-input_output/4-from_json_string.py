#!/usr/bin/python3
""" From JSON string to python object """
import json


def from_json_string(my_str):
    """ decodes JSON string to python object
    Args:
        my_str: string to be decoded
    """
    return json.loads(my_str)

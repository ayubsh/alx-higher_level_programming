#!/usr/bin/python3
""" Object to JSON string """
import json


def to_json_string(my_obj):
    """ endoces from python Object to JSON string
    Args:
        my_obj: Object to be stringfyed
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
""" Reads from json file """
import json


def load_from_json_file(filename):
    """ reads from json file, then turns it into python object
    Args:
        filename: name of the file
    """
    with open(filename) as file:
        return json.load(file)

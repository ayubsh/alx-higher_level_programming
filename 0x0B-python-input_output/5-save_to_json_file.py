#!/usr/bin/python3
""" Write file with json format """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to text file using JSON representation
    Args:
        my_obj: object to be written to the file
        filename: name of the file
    """
    with open(filename, "a") as file:
        file.write(json.dumps(my_obj))

#!/usr/bin/python3
""" Base model Class """
import json


class Base:
    """ The superclass where all other classes extends from
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for the base class
        Args:
            id: the id of the instance object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 0:
            return "[]"
        return json.dumps(list_dictionaries)

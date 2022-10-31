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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            list_objs: a list of instances who inherits of Base
        """
        f_name = cls.__name__ + ".json"
        print(f_name)
        with open(f_name, 'w', encoding="utf-8") as file:
            if list_objs is None or len(list_objs) <= 0:
                file.write(cls.to_json_string(list_objs))
            else:
                file.write(cls.to_json_string([obj.to_dictionary()
                                               for obj in list_objs]))

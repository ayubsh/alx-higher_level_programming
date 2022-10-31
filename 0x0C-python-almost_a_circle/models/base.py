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
        with open(f_name, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                i = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(i))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_strin
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """eturns an instance with all attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_ob = cls(1, 1)
            else:
                new_ob = cls(1)
            new_ob.update(**dictionary)
            return new_ob

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:
        """
        f_name = str(cls.__name__) + ".json"
        try:
            with open(f_name, "r") as jsonfile:
                l_obj = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in l_obj]
        except IOError:
            return []

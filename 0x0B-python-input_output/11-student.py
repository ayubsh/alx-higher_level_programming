#!/usr/bin/python3
""" Student to JSON """


class Student:
    """ it description of student """
    def __init__(self, first_name, last_name, age):
        """ constructor for the student class
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of the class
        Args:
            attrs: the attritubes to look for
        """
        if isinstance(attrs, list) and\
                all(type(e) == str for e in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json: a dictionary to replace attritubes
        """
        for key, value in json.items():
            setattr(self, key, value)

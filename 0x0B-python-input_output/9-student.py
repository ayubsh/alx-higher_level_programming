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

    def to_json(self):
        """ retrieves a dictionary representation of the class"""
        return self.__dict__

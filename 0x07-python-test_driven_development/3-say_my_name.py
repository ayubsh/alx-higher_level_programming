#!/usr/bin/python3
"""Say my name """


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>
    Args:
        first_name: first name
        last_name: second name
    Raises:
        TypeError: if either first_name or last_name is not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

#!/usr/bin/python3
"""
Module: say_my_name

This module provides a function to print a formatted full name,
with type validation for its inputs.
"""

def say_my_name(first_name, last_name=""):
    """
    Print a formatted string containing a person's name.

    The function validates that both first_name and last_name are strings.
    It prints the name in the format:
        My name is <first_name> <last_name>

    Args:
        first_name (str): The person's first name.
        last_name (str, optional): The person's last name. Defaults to "".

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

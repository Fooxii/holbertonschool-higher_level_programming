#!/usr/bin/python3
"""
Docstring for python-input_output.9-student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :param last_name: Description
        :param age: Description
        """
        first_name = first_name
        last_name = last_name
        age = age

    def to_json(self):
        """
        Docstring for to_json

        :param self: Description
        """
        return self.__dict__

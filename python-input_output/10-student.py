#!/usr/bin/python3
"""
Docstring for python-input_output.10-student
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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Docstring for to_json

        :param self: Description
        :param attrs: Description
        """
        if isinstance(attrs, list):
            new_dict = {}
            for attr in attrs:
                if isinstance(attr, str) and attr in self.__dict__:
                    new_dict[attr] = self.__dict__[attr]
            return new_dict

        return self.__dict__

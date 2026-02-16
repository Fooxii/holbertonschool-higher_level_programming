#!/usr/bin/python3
"""
Docstring for python-serialization.task_01_pickle
"""
import pickle


class CustomObject:
    """
    Docstring for CustomObject
    """
    def __init__(self, name, age, is_student):
        """
        Docstring for __init__

        :param self: Description
        :param name: Description
        :param age: Description
        :param is_student: Description
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Docstring for display

        :param self: Description
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Docstring for serialize

        :param self: Description
        :param filename: Description
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Docstring for deserialize

        :param cls: Description
        :param filename: Description
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None

#!/usr/bin/python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Docstring for serialize_and_save_to_file

    :param data: Description
    :param filename: Description
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_diserialize(filename):
    """
    Docstring for load_and_diserialize

    :param filename: Description
    """
    with open(filename, 'r') as file:
        return json.load(file)

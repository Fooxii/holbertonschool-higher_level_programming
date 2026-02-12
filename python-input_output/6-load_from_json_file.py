#!/usr/bin/python3
"""
Docstring for python-input_output.6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Docstring for load_from_json_file

    :param filename: Description
    """
    with open(filename, 'r', encoding="utf-8") as file:
        my_obj = json.load(file)
        return my_obj

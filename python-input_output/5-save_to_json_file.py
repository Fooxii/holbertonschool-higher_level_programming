#!/usr/bin/python3
"""
Docstring for python-input_output.5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Docstring for save_to_json_file

    :param my_obj: Description
    :param filename: Description
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(json.dumps(my_obj))

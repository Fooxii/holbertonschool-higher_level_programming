#!/usr/bin/python3
"""
Docstring for python-input_output.2-append_write
"""


def write_file(filename="", text=""):
    """
    Docstring for write_file

    :param filename: Description
    :param text: Description
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)

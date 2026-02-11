#!/usr/bin/python3
"""
Docstring for python-input_output.0-read_file
"""

def read_file(filename=""):
    """
    Docstring for read_file
    
    :param filename: Description
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")

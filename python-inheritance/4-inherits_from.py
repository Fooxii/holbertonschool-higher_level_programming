#!/usr/bin/python3
"""
Docstring for python-inheritance.4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    Docstring for inherits_from

    :param obj: Description
    :param a_class: Description
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False

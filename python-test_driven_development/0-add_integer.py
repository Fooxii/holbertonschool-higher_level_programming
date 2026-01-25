#!/usr/bin/python3
"""
This module provides a function to add two numbers.

Only integers and floats are accepted. Floats are cast to integers
before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number to add.
        b (int or float, optional): Second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b after casting them to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b

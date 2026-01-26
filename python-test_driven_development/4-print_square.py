#!/usr/bin/python3
"""
Module: print_square

This module provides a function to print a square made of the '#' character.
"""


def print_square(size):
    """
    Print a square with the character '#'.

    The square will have dimensions size x size.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

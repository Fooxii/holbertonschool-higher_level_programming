#!/usr/bin/python3
"""
Docstring for python-input_output.12-pascal_triangle
"""


def pascal_triangle(n):
    """
    Docstring for pascal_triangle

    :param n: Description
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if triangle:
            prev = triangle[-1]
            for j in range(len(prev) - 1):
                row.append(prev[j] + prev[j + 1])
            row.append(1)

        triangle.append(row)

    return triangle

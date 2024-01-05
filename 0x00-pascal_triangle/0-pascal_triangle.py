#!/usr/bin/python3
"""Module to print list of ints of pascals triangle"""


def pascal_triangle(n):
    """Function displays list of lists of ints representing
    pascal's triangle of n"""
    triangle = []

    if n <= 0:
        return []

    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        if i > 0:
            row.append(1)

        triangle.append(row)

    return triangle

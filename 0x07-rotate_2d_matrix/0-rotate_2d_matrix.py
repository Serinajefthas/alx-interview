#!/usr/bin/python3
"""Rotate 2d matrix 90 degrees"""


def rotate_2d_matrix(matrix):
    """roate 2d matrix 90 degrees clockwise"""
    length = len(matrix)
    for row in range(length//2):
        first = row
        last = length - 1 - row

        for i in range(first, last):
            """save top element"""
            top = matrix[row][i]
            """move left elem to top"""
            matrix[row][i] = matrix[-i - 1][row]
            """move bottom to left"""
            matrix[-i - 1][row] = matrix[-row - 1][-i - 1]
            """move right to bottom"""
            matrix[-row - 1][-i - 1] = matrix[i][-row - 1]
            """top to right"""
            matrix[i][-row - 1] = top

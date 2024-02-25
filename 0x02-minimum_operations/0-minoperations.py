#!/usr/bin/python3
"""Module calculates fewest num operations needed for n num of H characters
"""


def minOperations(n):
    if n <= 1:
        return 0

    min_ops = n
    for i in range(2, int(n**0.5) + 1):
        """from 2 to root n inclusive"""
        if n % i == 0:
            """ if i factor of n"""
            min_ops = min(min_ops, i + minOperations(n // i))

    if min_ops == n:
        return n

    return min_ops

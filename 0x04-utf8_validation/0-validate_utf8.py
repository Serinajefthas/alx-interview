#!/usr/bin/python3
"""Module to check validity of utf-8 encoding"""


def count_ones(byte):
    """ counts leading 1s in byte"""
    cnt = 0
    mask = 1 << 7  # shifts bit rep of 1 seven pos to left
    while byte & mask:
        cnt += 1
        mask >>= 1
    return cnt


def validUTF8(data):
    """checks if data is valid utf-8 encoding"""
    num_bytes = 0
    i = 0
    while i < len(data):
        if num_bytes == 0:
            num_bytes = count_ones(data[i])
            if num_bytes == 1 or num_bytes > 4:
                return False  # too many bites for utf8 rules
            if num_bytes == 0:
                i += 1
                continue
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        i += 1
        num_bytes -= 1

    return num_bytes == 0

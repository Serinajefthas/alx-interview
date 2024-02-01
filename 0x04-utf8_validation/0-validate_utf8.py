#!/usr/bin/python3
"""Module to check validity of utf-8 encoding"""



def validUTF8(data):
    """Function checks utf-8 validity of string"""
    def is_byte(byte):
        """checks if byte follows utf8 encoding rules"""
        return 128 <= byte <= 191

    def count_ones(byte):
        """ counts leading 1s in byte"""
        cnt = 0
        mask = 1 << 7 #shifts bit rep of 1 seven pos to left
        while byte & mask:
            cnt += 1
            mask >>= 1
        return cnt

    i = 0
    while i < len(data):
        num_bytes = count_ones(data[i])
        if num_bytes == 1 or num_bytes > 4 or i + num_bytes > len(data):
            return False #too many bites for utf8 rules

        for j in range(1, num_bytes):
            if not is_byte(data[i + j]):
                return False

        i += num_bytes 

    return True        

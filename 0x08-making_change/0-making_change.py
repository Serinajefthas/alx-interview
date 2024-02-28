#!/usr/bin/python3
"""Module to determine fewest number coins for total amt"""
import sys


def makeChange(coins, total):
    """Function to determine fewest number coins for total amt"""
    if total <= 0:
        return 0
    size = len(coins)

    minCoins = [0 for i in range(total + 1)]
    for i in range(1, total + 1):
        """initialise array values to infinity"""
        minCoins[i] = sys.maxsize

    for i in range(1, total + 1):
        """iterate through coins < i"""
        for j in range(size):
            if (coins[j] <= i):
                sub_res = minCoins[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < minCoins[i]):
                    minCoins[i] = sub_res + 1

    if minCoins[total] == sys.maxsize:
        return -1

    return minCoins[total]

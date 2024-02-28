#!/usr/bin/python3
"""Module to determine fewest number coins for total amt"""
import sys


def makeChange(coins, total):
    """Function to determine fewest number coins for total amt"""
    if total <= 0:
        return 0

    """set all values to pos infinity"""
    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        for amt in range(coin, total + 1):
            minCoins[amt] = min(minCoins[amt], minCoins[amt - coin] + 1)
    """if value still infinity then total not possible"""
    if minCoins[total] == float('inf'):
        return -1

    """Works but less efficient
    size = len(coins)

    minCoins = [0 for i in range(total + 1)]
    for i in range(1, total + 1):
        initialise array values to infinity
        minCoins[i] = sys.maxsize

    for i in range(1, total + 1):
        iterate through coins < i
        for j in range(size):
            if (coins[j] <= i):
                sub_res = minCoins[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < minCoins[i]):
                    minCoins[i] = sub_res + 1

    if minCoins[total] == sys.maxsize:
        return -1"""
    return minCoins[total]

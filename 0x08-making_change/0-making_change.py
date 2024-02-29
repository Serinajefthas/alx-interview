#!/usr/bin/python3
"""Module to determine fewest number coins for total amt"""
import sys


def makeChange(coins, total):
    """Function to determine fewest number coins for total amt"""
    if total <= 0:
        return 0
    coins.sort(reverse=true)
    coin_cnt = 0

    for coin in coins:
        if coin > total:
            continue
        cnt = total // coin
        total -= cnt * coin
        coin_cnt += cnt
        if total == 0:
            break
    if total > 0:
        return -1
    return coin_cnt
    """set all values to pos infinity
    minCoins = [float('inf')] * (total + 1)
    minCoins[0] = 0

    for coin in coins:
        for amt in range(coin, total + 1):
            minCoins[amt] = min(minCoins[amt], minCoins[amt - coin] + 1)
    if value still infinity then total not possible
    if minCoins[total] == float('inf'):
        return -1
    return minCoins[total]
"""

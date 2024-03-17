#!/usr/bin/python3
"""Module that runs function for prime game"""


def isWinner(x, nums):
    """Prime game function using Sieve of Eratothenes"""
    if x < 1 or not nums:
        return -1

    idx = maria_wins = ben_wins = 0

    for round in range(x):
        numbers = [n for n in range(2, nums[round] + 1)]
        """sieve of erathosas"""
        while (idx < len(numbers)):
            prime = numbers[idx]
            sieve_idx = idx + prime
            while (sieve_idx < len(numbers)):
                numbers.pop(sieve_idx)
                sieve_idx += prime - 1
            idx += 1

        cnt_prime = len(numbers)
        if cnt_prime and cnt_prime % 2:
            maria_wins += 1
        else:
            ben_wins += 1

    if ben_wins == maria_wins:
        return None
    return 'Ben' if ben_wins > maria_wins else 'Maria'

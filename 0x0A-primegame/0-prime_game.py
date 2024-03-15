#!/usr/bin/python3
"""Module that runs function for prime game"""


def isWinner(x, nums):
    """Prime game function using Sieve of Eratothenes"""
    def sieve_of_e(n):
        """computes all primes no.s up to given no."""
        primes = [True] * (n+1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1
        return [i for i in range(n+1) if primes[i]]

    maria_wins = ben_wins = 0
    for i in nums:
        primes = sieve_of_e(i)

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"

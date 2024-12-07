#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


import math
import bisect


def sieve_of_eratosthenes(max_num):
    sieve = bytearray([True]) * (max_num + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(max_num) + 1):
        if sieve[p]:
            sieve[p * p : max_num + 1 : p] = b"\x00" * len(
                sieve[p * p : max_num + 1 : p]
            )
    return [p for p, is_prime in enumerate(sieve) if is_prime]


def main():
    limit = int(input())
    prime_numbers = sieve_of_eratosthenes(2000000)
    numbers_with_9_divisors = 0

    max_p_eight = int(limit ** (1 / 8))
    numbers_with_9_divisors += bisect.bisect_right(prime_numbers, max_p_eight)

    sqrt_limit = math.isqrt(limit)
    for index_p, prime_p in enumerate(prime_numbers):
        if prime_p > sqrt_limit:
            break
        prime_p_squared = prime_p * prime_p
        if prime_p_squared > limit:
            break
        max_prime_q = math.isqrt(limit // prime_p_squared)
        if max_prime_q < prime_p:
            continue
        upper_bound_q_index = bisect.bisect_right(prime_numbers, max_prime_q)
        valid_q_count = upper_bound_q_index - (index_p + 1)
        numbers_with_9_divisors += valid_q_count

    print(numbers_with_9_divisors)


if __name__ == "__main__":
    main()

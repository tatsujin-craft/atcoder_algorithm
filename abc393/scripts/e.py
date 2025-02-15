#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_max_gcds(k, a_list):
    if k == 1:
        return a_list

    max_a = max(a_list)
    freq = [0] * (max_a + 1)
    for a in a_list:
        freq[a] += 1

    count_divisible = [0] * (max_a + 1)
    upper_limit = max_a + 1
    for divisor in range(1, upper_limit):
        total = 0
        for multiple in range(divisor, upper_limit, divisor):
            total += freq[multiple]
        count_divisible[divisor] = total

    max_gcd = [0] * (max_a + 1)
    for divisor in range(max_a, 0, -1):
        if count_divisible[divisor] >= k:
            for multiple in range(divisor, upper_limit, divisor):
                if max_gcd[multiple] == 0:
                    max_gcd[multiple] = divisor

    max_gcds = [max_gcd[a] for a in a_list]
    return max_gcds


def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))

    results = get_max_gcds(k, a_list)
    print("\n".join(map(str, results)))


if __name__ == "__main__":
    main()

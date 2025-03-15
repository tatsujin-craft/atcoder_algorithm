#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

import math


def find_cube_pair(n):
    # x^3 - y^3 = n
    # n = d * (3*y^2 + 3*d*y + d^2)
    # M = n//d
    # D = 3*(4*M - d^2)

    limit = int(round(n ** (1 / 3))) + 1
    for d in range(1, limit + 1):
        if n % d != 0:
            continue

        M = n // d
        D = 3 * (4 * M - d * d)
        if D < 0:
            continue

        t = math.isqrt(D)
        if t * t != D:
            continue

        if t < 3 * d:
            continue
        if (t - 3 * d) % 6 != 0:
            continue

        y = (t - 3 * d) // 6
        if y <= 0:
            continue
        x = y + d
        return x, y
    return -1


def main():
    n = int(input())

    result = find_cube_pair(n)
    if result == -1:
        print(-1)
    else:
        print(result[0], result[1])


if __name__ == "__main__":
    main()

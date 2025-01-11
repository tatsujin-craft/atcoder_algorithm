#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_final_stones_count(N, initial_stones):
    stones_count = [0] * N
    diff = [0] * (N + 2)
    active_adults = 0

    for year in range(1, N + 1):
        active_adults += diff[year]
        stones_count[year - 1] = initial_stones[year - 1] + active_adults
        give_count = min(stones_count[year - 1], N - year)
        stones_count[year - 1] -= give_count

        if year + 1 <= N:
            diff[year + 1] += 1

        stop_year = year + give_count
        if stop_year + 1 <= N:
            diff[stop_year + 1] -= 1

    return stones_count


def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = get_final_stones_count(N, A)
    print(*result)


if __name__ == "__main__":
    main()

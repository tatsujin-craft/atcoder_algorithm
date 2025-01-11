#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_kagamimochi_pairs_count(mochi_list):
    total_mochis = len(mochi_list)
    half_mochi_count = total_mochis // 2
    small_index = 0
    large_index = half_mochi_count
    pairs_count = 0

    while small_index < half_mochi_count and large_index < total_mochis:
        if 2 * mochi_list[small_index] <= mochi_list[large_index]:
            pairs_count += 1
            small_index += 1
            large_index += 1
        else:
            large_index += 1

    return pairs_count


def main():
    N = int(input())
    mochi_list = list(map(int, input().split()))

    kagamimochi_pairs_count = get_kagamimochi_pairs_count(mochi_list)
    print(kagamimochi_pairs_count)


if __name__ == "__main__":
    main()

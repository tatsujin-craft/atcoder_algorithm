#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def count_min_swaps(s):
    target_positions = []
    for index, char in enumerate(s):
        if char == "1":
            target_positions.append(index)

    count_of_ones = len(target_positions)
    if count_of_ones <= 1:
        return 0

    offset_list = [target_positions[i] - i for i in range(count_of_ones)]
    offset_list.sort()

    median_offset = offset_list[count_of_ones // 2]
    min_swaps = 0
    for offset in offset_list:
        min_swaps += abs(offset - median_offset)

    return min_swaps


def main():
    n = int(input())
    s = input()

    result = count_min_swaps(s)
    print(result)


if __name__ == "__main__":
    main()

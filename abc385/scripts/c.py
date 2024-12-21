#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


from collections import defaultdict


def get_max_length(heights):
    height_to_indices = defaultdict(list)
    for index, height in enumerate(heights):
        height_to_indices[height].append(index)

    max_length = 1
    for height, indices in height_to_indices.items():
        count = len(indices)
        if count == 1:
            continue
        dp = [{} for _ in range(count)]
        for current in range(count):
            for previous in range(current):
                difference = indices[current] - indices[previous]
                if difference in dp[previous]:
                    dp[current][difference] = dp[previous][difference] + 1
                else:
                    dp[current][difference] = 2
                if dp[current][difference] > max_length:
                    max_length = dp[current][difference]
    return max_length


def main():
    _ = int(input())
    building_heights = list(map(int, input().split()))

    max_length = get_max_length(building_heights)
    print(max_length)


if __name__ == "__main__":
    main()

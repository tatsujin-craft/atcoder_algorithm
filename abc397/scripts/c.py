#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_max_variety_sum(n, seq):
    prefix = [0] * n
    seen = set()
    count = 0
    for i in range(n):
        if seq[i] not in seen:
            seen.add(seq[i])
            count += 1
        prefix[i] = count

    suffix = [0] * n
    seen = set()
    count = 0
    for i in range(n - 1, -1, -1):
        if seq[i] not in seen:
            seen.add(seq[i])
            count += 1
        suffix[i] = count

    max_variety_sum = 0
    for i in range(n - 1):
        max_variety_sum = max(max_variety_sum, prefix[i] + suffix[i + 1])
    return max_variety_sum


def main():
    n = int(input())
    seq = list(map(int, input().split()))

    result = get_max_variety_sum(n, seq)
    print(result)


if __name__ == "__main__":
    main()

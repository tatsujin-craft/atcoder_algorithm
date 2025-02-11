#!/usr/bin/env python3
"""
Script Name: prac_a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    missing_nums = []
    for i in range(1, N + 1):
        if i not in A:
            missing_nums.append(i)

    print(len(missing_nums))
    print(*missing_nums)


if __name__ == "__main__":
    main()

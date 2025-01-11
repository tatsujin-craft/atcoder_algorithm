#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

import bisect


def main():
    n = int(input())
    mochi_list = list(map(int, input().split()))
    mochi_list.sort()

    kagamimochi_count = 0
    for i in range(n):
        kagamimochi_count += bisect.bisect_right(mochi_list, mochi_list[i] // 2, 0, i)

    print(kagamimochi_count)


if __name__ == "__main__":
    main()

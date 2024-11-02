#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

from collections import Counter


def count_pairs(a1, a2, a3, a4):
    counts = Counter([a1, a2, a3, a4])
    return sum(v // 2 for v in counts.values())


def main():
    a1, a2, a3, a4 = map(int, input().split())
    print(count_pairs(a1, a2, a3, a4))


if __name__ == "__main__":
    main()

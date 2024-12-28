#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


from collections import Counter


def main():
    A, B, C, D = map(int, input().split())
    count = Counter([A, B, C, D])

    if len(count) == 2:
        values = sorted(count.values())
        if values == [1, 3] or values == [2, 2]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()

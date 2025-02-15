#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    s = input()
    n = len(s)

    count = 0
    for i in range(1, n):
        for j in range(n - 2 * i):
            if s[j] == "A" and s[j + i] == "B" and s[j + 2 * i] == "C":
                count += 1
    print(count)


if __name__ == "__main__":
    main()

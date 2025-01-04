#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    x = int(input())

    total = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j != x:
                total += i * j
    print(total)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, c1, c2 = input().split()
    S = input()

    result_chars = []
    for c in S:
        if c == c1:
            result_chars.append(c)
        else:
            result_chars.append(c2)

    print("".join(result_chars))


if __name__ == "__main__":
    main()

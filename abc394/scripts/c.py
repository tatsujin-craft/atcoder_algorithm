#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    s = list(input())

    n = len(s)
    for i in range(n - 2, -1, -1):
        if s[i] == "W" and s[i + 1] == "A":
            s[i], s[i + 1] = "A", "C"

    result = "".join(s)
    print(result)


if __name__ == "__main__":
    main()

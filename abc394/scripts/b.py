#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n = int(input())
    s = [input() for _ in range(n)]

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if len(s[i]) > len(s[j]):
                s[i], s[j] = s[j], s[i]

    result = "".join(s)
    print(result)


if __name__ == "__main__":
    main()

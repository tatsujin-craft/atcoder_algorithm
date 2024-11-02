#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def output_sequence_b(n, a):
    last_seen = {}
    b = []
    for i in range(n):
        if a[i] in last_seen:
            b.append(last_seen[a[i]])
        else:
            b.append(-1)
        last_seen[a[i]] = i + 1
    print(" ".join(map(str, b)))


def main():
    n = int(input())
    a = list(map(int, input().split()))

    output_sequence_b(n, a)


if __name__ == "__main__":
    main()

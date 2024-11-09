#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, K = map(int, input().split())
    S = list(input())
    count = 0
    i = 0
    while i <= N - K:
        if S[i : i + K] == ["O"] * K:
            count += 1
            S[i : i + K] = ["X"] * K
            i += K
        else:
            i += 1
    print(count)


if __name__ == "__main__":
    main()

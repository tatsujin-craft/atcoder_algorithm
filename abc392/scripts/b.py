#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A_set = set(A)

    result = [i for i in range(1, N + 1) if i not in A_set]
    print(len(result))
    if result:
        print(" ".join(map(str, result)))
    else:
        print("")


if __name__ == "__main__":
    main()

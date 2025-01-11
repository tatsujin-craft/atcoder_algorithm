#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, D = map(int, input().split())
    T = []
    L = []
    for _ in range(N):
        t, l = map(int, input().split())
        T.append(t)
        L.append(l)

    for k in range(1, D + 1):
        max_weight = max(T[i] * (L[i] + k) for i in range(N))
        print(max_weight)


if __name__ == "__main__":
    main()

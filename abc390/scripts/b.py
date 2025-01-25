#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if N <= 2:
        print("Yes")
    else:
        is_geometric_sequence = True
        for i in range(2, N):
            if A[i] * A[i - 2] != A[i - 1] ** 2:
                is_geometric_sequence = False
                break
        if is_geometric_sequence:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

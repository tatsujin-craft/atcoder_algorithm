#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    A = list(map(int, input().split()))

    for i in range(4):
        A[i], A[i + 1] = A[i + 1], A[i]
        if A == sorted(A):
            print("Yes")
            return
        A[i], A[i + 1] = A[i + 1], A[i]
    print("No")


if __name__ == "__main__":
    main()

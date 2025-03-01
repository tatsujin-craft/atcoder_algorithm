#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n = int(input())
    A = list(map(int, input().split()))

    result = "Yes"
    for i in range(n - 1):
        if A[i] >= A[i + 1]:
            result = "No"
            break

    print(result)


if __name__ == "__main__":
    main()

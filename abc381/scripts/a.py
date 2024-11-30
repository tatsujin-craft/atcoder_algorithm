#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N = int(input())
    S = input()

    # Check odd number
    if N % 2 == 1:
        mid = (N + 1) // 2
        if (
            S[: mid - 1] == "1" * (mid - 1)
            and S[mid - 1] == "/"
            and S[mid:] == "2" * (N - mid)
        ):
            print("Yes")
        else:
            print("No")
    else:
        print("No")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, R = map(int, input().split())
    contests = [tuple(map(int, input().split())) for _ in range(N)]

    for D, A in contests:
        if D == 1 and 1600 <= R <= 2799:
            R += A
        elif D == 2 and 1200 <= R <= 2399:
            R += A

    print(R)


if __name__ == "__main__":
    main()

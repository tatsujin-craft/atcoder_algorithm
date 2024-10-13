#!/usr/bin/env python3
"""
Script Name: prac_a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N = int(input())
    S = input()
    print(S)

    count = 0
    for i in range(N - 2):
        if S[i] == "#" and S[i + 1] == "." and S[i + 2] == "#":
            count += 1
    print(count)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, D = map(int, input().split())
    s_list = list(input())

    for i in range(N - 1, -1, -1):
        if s_list[i] == "@" and D > 0:
            s_list[i] = "."
            D -= 1
    print("".join(s_list))


if __name__ == "__main__":
    main()

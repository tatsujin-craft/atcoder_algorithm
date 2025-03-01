#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    last_positions_dict = {}
    min_length = float("inf")
    for i, a in enumerate(a_list):
        if a in last_positions_dict:
            min_length = min(min_length, i - last_positions_dict[a] + 1)
        last_positions_dict[a] = i

    if min_length != float("inf"):
        print(min_length)
    else:
        print(-1)


if __name__ == "__main__":
    main()

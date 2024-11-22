#!/usr/bin/env python3
"""
Script Name: prac_b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    S = input()
    print(S)

    num_list = []
    dash_count = 0

    for char in S[1:]:
        if char == "|":
            num_list.append(dash_count)
            dash_count = 0

        elif char == "-":
            dash_count += 1

    print(*num_list)


if __name__ == "__main__":
    main()

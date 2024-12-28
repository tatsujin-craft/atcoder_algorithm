#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_min_button_presses(S):
    length = len(S)
    count = 0
    i = 0

    while i < length:
        if i + 2 <= length and S[i : i + 2] == "00":
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count


def main():
    S = input()

    min_button_presses = get_min_button_presses(S)
    print(min_button_presses)


if __name__ == "__main__":
    main()

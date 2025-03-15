#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    s = input()
    length = len(s)

    if length % 2 == 0:
        target_length = length
    else:
        target_length = length + 1

    while True:
        target_pattern = "io" * (target_length // 2)
        i = 0
        for c in target_pattern:
            if i < length and c == s[i]:
                i += 1
        if i == length:
            inserted_length = target_length - length
            print(inserted_length)
            break
        target_length += 2


if __name__ == "__main__":
    main()

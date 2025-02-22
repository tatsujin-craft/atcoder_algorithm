#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    s = input()

    filtered_str = []
    for c in s:
        if c == "2":
            filtered_str.append(c)

    result = "".join(filtered_str)
    print(result)


if __name__ == "__main__":
    main()

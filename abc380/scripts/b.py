#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    S = input()
    result = []
    count = 0
    inside_pipe = False

    for char in S:
        if char == "|":
            if inside_pipe:
                result.append(count)
                count = 0
            inside_pipe = True

        elif char == "-" and inside_pipe:
            count += 1

    print(*result)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def is_colorful_bracket_sequence(s):
    stack = []
    pairs = {")": "(", "]": "[", ">": "<"}
    for c in s:
        if c in "([<":
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def main():
    s = input()

    judge = is_colorful_bracket_sequence(s)
    if judge:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

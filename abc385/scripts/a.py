#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    a, b, c = map(int, input().split())

    if a + b == c:
        print("Yes")
    elif b + c == a:
        print("Yes")
    elif a + c == b:
        print("Yes")
    elif a == b == c:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

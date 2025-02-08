#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    A1, A2, A3 = map(int, input().split())

    if (A2 * A3 == A1) or (A1 * A3 == A2) or (A1 * A2 == A3):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

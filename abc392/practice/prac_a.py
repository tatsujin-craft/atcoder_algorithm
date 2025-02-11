#!/usr/bin/env python3
"""
Script Name: prac_a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    a1, a2, a3 = map(int, input().split())

    if (a1 * a2 == a3) or (a1 * a3 == a2) or (a2 * a3 == a1):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

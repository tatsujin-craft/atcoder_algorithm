#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    X = int(input())

    N = 1
    tmp = 1
    while tmp < X:
        N += 1
        tmp *= N
    print(N)


if __name__ == "__main__":
    main()

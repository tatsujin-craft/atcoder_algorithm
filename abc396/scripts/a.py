#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    for i in range(n - 2):
        if a_list[i] == a_list[i + 1] == a_list[i + 2]:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()

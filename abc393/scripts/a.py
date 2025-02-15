#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    s1, s2 = input().split()

    if s1 == "fine" and s2 == "fine":
        oyster_num = 4
    elif s1 == "fine" and s2 == "sick":
        oyster_num = 3
    elif s1 == "sick" and s2 == "fine":
        oyster_num = 2
    else:
        oyster_num = 1

    print(oyster_num)


if __name__ == "__main__":
    main()

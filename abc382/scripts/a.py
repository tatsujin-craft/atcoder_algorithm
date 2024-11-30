#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, D = map(int, input().split())
    S = input()

    init_empty_box_num = N - S.count("@")
    empty_box_num = D + init_empty_box_num
    print(empty_box_num)


if __name__ == "__main__":
    main()

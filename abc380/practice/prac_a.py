#!/usr/bin/env python3
"""
Script Name: prac_a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n_str = input()
    print(n_str)

    if n_str.count("1") == 1 and n_str.count("2") == 2 and n_str.count("3") == 3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Description: Leap year days
Author: tatsujin
Date: 2024-10-13
"""


def check_leap_year(Y):
    is_leap_year = False
    if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
        is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


def main():
    Y = int(input())

    if check_leap_year(Y):
        print(366)
    else:
        print(365)


if __name__ == "__main__":
    main()

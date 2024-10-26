#!/usr/bin/env python3
"""
Script Name: prac_b.py
Description: This script is a template.
Author: tatsujin
Date: 2024-10-26
"""


from decimal import Decimal


# WA 2/22, AC 20/22
# ex) 50.000 → NG:5E+1, OK:50
def process_decimal(value):
    x = Decimal(value)
    print(x.normalize())


# AC
def refined_process_decimal(value):
    x = Decimal(value)
    print(f"{x.normalize():f}")


# AC
def process_float(value):
    X = float(value)
    print(f"{X:.3f}".rstrip("0").rstrip("."))


# AC
def remove_trailing_zeros(value):
    while value.endswith("0"):
        value = value[:-1]
    if value.endswith("."):
        value = value[:-1]
    print(value)


def main():
    value = input()
    process_decimal(value)
    refined_process_decimal(value)
    process_float(value)
    remove_trailing_zeros(value)


if __name__ == "__main__":
    main()

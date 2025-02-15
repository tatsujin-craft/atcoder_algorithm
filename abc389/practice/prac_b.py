#!/usr/bin/env python3
"""
Script Name: prac_b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def calc_fact(n):
    fact_val = 1
    for i in range(1, n + 1):
        fact_val *= i
    return fact_val


def calc_fact_recursive(n):
    if n == 1:
        return 1
    fact_val = n * calc_fact_recursive(n - 1)
    return fact_val


def main():
    x = int(input())

    n = 1
    fact = 1
    while 1:
        # fact *= n
        fact = calc_fact(n)
        # fact = calc_fact_recursive(n)
        print(f"N: {n}, Factorial: {fact}")
        if fact == x:
            print(n)
            exit()
        elif fact > x:
            exit()
        n += 1


if __name__ == "__main__":
    main()

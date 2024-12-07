#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N = int(input())
    water_additions = [tuple(map(int, input().split())) for _ in range(N)]
    water_additions.sort()
    T_prev = 0

    V = 0
    for T, V_add in water_additions:
        T_delta = T - T_prev
        V = max(V - T_delta, 0)
        V += V_add
        T_prev = T

    print(V)


if __name__ == "__main__":
    main()

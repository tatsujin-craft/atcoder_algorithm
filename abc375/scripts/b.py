#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


import math


def calculate_total_cost(N, points):
    total_cost = 0.0
    x_prev, y_prev = 0, 0
    for x, y in points:
        total_cost += math.sqrt((x - x_prev) ** 2 + (y - y_prev) ** 2)
        x_prev, y_prev = x, y
    total_cost += math.sqrt((0 - x_prev) ** 2 + (0 - y_prev) ** 2)
    return total_cost


def main():
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print(calculate_total_cost(N, points))


if __name__ == "__main__":
    main()

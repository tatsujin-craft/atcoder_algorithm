#!/usr/bin/env python3
"""
Script Name: prac_b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

import math


def calc_cost(prev_x, prev_y, x, y):
    cost = math.sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    print(f"point: ({prev_x}, {prev_y}) => ({x}, {y}), cost: {cost}")
    return cost


def get_result(N, points):
    prev_x, prev_y = 0, 0
    cost_sum = 0

    # (prev_x, prev_y) => (x, y)
    for i in range(N):
        cost_sum += calc_cost(prev_x, prev_y, points[i][0], points[i][1])
        print(f"sum: {cost_sum}\n")
        prev_x = points[i][0]
        prev_y = points[i][1]

    # (Xn, Yn) => (0, 0)
    cost_sum += calc_cost(points[N - 1][0], points[N - 1][1], 0, 0)
    print(f"sum: {cost_sum}\n")

    return cost_sum


def main():
    N = int(input())
    # List comprehension
    points = [list(map(int, input().split())) for _ in range(N)]
    print(points, "\n")

    cost_sum = get_result(N, points)
    print(cost_sum)


if __name__ == "__main__":
    main()

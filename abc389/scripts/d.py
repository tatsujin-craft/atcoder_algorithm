#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_square_count_in_circle(R):
    # Recursive
    def is_corner_inside_circle(i, j):
        dx = 2 * i + 1
        dy = 2 * j + 1
        return dx * dx + dy * dy <= 4 * (R**2)

    # Origin
    sum_origin = 1 if is_corner_inside_circle(0, 0) else 0

    # X axis
    sum_x_axis = 0
    i = 1
    while is_corner_inside_circle(i, 0):
        sum_x_axis += 1
        i += 1

    # Y axis
    i_stop = i - 1
    sum_y_axis = 0
    j = 1
    while is_corner_inside_circle(0, j):
        sum_y_axis += 1
        j += 1

    # Quater
    j_stop = j - 1
    sum_quater = 0
    j = j_stop
    for i in range(1, i_stop + 1):
        while j >= 1 and not is_corner_inside_circle(i, j):
            j -= 1
        sum_quater += j

    # Total
    total_count = 4 * sum_quater + 2 * sum_x_axis + 2 * sum_y_axis + sum_origin
    return total_count


def main():
    R = int(input())

    square_count = get_square_count_in_circle(R)
    print(square_count)


if __name__ == "__main__":
    main()

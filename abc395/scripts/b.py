#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n = int(input())

    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(" ")
        grid.append(row)

    for i in range(1, n + 1):
        j = n + 1 - i
        if i <= j:
            if i % 2 == 1:
                color = "#"
            else:
                color = "."
            for row_index in range(i - 1, j):
                for col_index in range(i - 1, j):
                    grid[row_index][col_index] = color

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def check_black_rectangle_possible(H, W, grid):
    black_cells = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                black_cells.append((i, j))

    if not black_cells:
        return True
    min_row = min(i for i, _ in black_cells)
    max_row = max(i for i, _ in black_cells)
    min_col = min(j for _, j in black_cells)
    max_col = max(j for _, j in black_cells)

    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if grid[i][j] == ".":
                return False

    for i in range(H):
        for j in range(W):
            if not (min_row <= i <= max_row and min_col <= j <= max_col):
                if grid[i][j] == "#":
                    return False
    return True


def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    is_rectangle_possible = check_black_rectangle_possible(H, W, grid)
    if is_rectangle_possible:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

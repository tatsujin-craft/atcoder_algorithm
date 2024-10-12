#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def rotate_grid(n, grid):
#     for i in range(n // 2):
#         for x in range(i, n - i - 1):
#             y = n - i - 1
#             temp = grid[x][i]
#             grid[x][i] = grid[y][x]
#             grid[y][x] = grid[n - x - 1][y]
#             grid[n - x - 1][y] = grid[i][n - x - 1]
#             grid[i][n - x - 1] = temp
#     return grid


# def replace_grid_colors(n, grid):
#     for i in range(n // 2):
#         for x in range(i + 1, n - i - 1):
#             for y in range(i + 1, n - i - 1):
#                 grid[x][y] = grid[y][n - x - 1]
#     return grid


# def replace_grid_colors(n, grid):
#     for i in range(n // 2):
#         for x in range(i + 1, n - i - 1):
#             for y in range(i + 1, n - i - 1):
#                 grid[x][y] = grid[y][n - 1 - x]
#     return grid


def replace_grid_colors(n, grid):
    for i in range(n // 2):
        for x in range(i, n - i):
            for y in range(i, n - i):
                if x != y and y != n - x - 1:
                    grid[x][y] = grid[y][n - 1 - x]
    return grid


def main():
    # n = int(input())
    # grid = [list(input().strip()) for _ in range(n)]
    # result = replace_grid_colors(n, grid)

    # for row in result:
    #     print("".join(row))

    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    result = replace_grid_colors(n, grid)

    for row in result:
        print("".join(row))


if __name__ == "__main__":
    main()

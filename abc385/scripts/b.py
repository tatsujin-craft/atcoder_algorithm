#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    H, W, X, Y = map(int, input().split())
    grid = [input().strip() for _ in range(H)]
    T = input().strip()

    visited = set()
    if grid[X - 1][Y - 1] == "@":
        visited.add((X, Y))

    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    for move in T:
        dx, dy = directions.get(move, (0, 0))
        nx, ny = X + dx, Y + dy
        if 1 <= nx <= H and 1 <= ny <= W and grid[nx - 1][ny - 1] != "#":
            X, Y = nx, ny
            if grid[X - 1][Y - 1] == "@":
                visited.add((X, Y))
    print(X, Y, len(visited))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    H, W, D = map(int, input().split())
    grid = [input() for _ in range(H)]
    floor = []

    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                floor.append((i, j))

    n = len(floor)
    covered = []
    for idx in range(n):
        ci, cj = floor[idx]
        mask = 0
        for k in range(n):
            fi, fj = floor[k]
            if abs(ci - fi) + abs(cj - fj) <= D:
                mask |= 1 << k
        covered.append(mask)

    max_humid_floor = 0
    for i in range(n):
        for j in range(i + 1, n):
            combined = covered[i] | covered[j]
            count = bin(combined).count("1")
            if count > max_humid_floor:
                max_humid_floor = count

    print(max_humid_floor)


if __name__ == "__main__":
    main()

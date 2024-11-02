#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, remaining_moves, H, W, grid):
    if remaining_moves == 0:
        return 1
    count = 0
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == ".":
            grid[x][y] = "#"
            count += dfs(nx, ny, remaining_moves - 1, H, W, grid)
            grid[x][y] = "."
    return count


def main():
    H, W, K = map(int, input().split())
    grid = [list(input().strip()) for _ in range(H)]
    total_paths = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                total_paths += dfs(i, j, K, H, W, grid)
    print(total_paths)


if __name__ == "__main__":
    main()


# DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# def count_paths(H, W, K, grid):
#     dp = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
#     start_found = False

#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == "." and not start_found:
#                 dp[i][j][0] = 1
#                 start_found = True
#                 break
#         if start_found:
#             break

#     for m in range(1, K + 1):
#         for i in range(H):
#             for j in range(W):
#                 if grid[i][j] == ".":
#                     for dx, dy in DIRECTIONS:
#                         ni, nj = i + dx, j + dy
#                         if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == ".":
#                             dp[i][j][m] += dp[ni][nj][m - 1]

#     total_paths = 0
#     for i in range(H):
#         for j in range(W):
#             if grid[i][j] == ".":
#                 total_paths += dp[i][j][K]

#     return total_paths


# def main():
#     H, W, K = map(int, input().split())
#     grid = [list(input().strip()) for _ in range(H)]
#     print(count_paths(H, W, K, grid))


# if __name__ == "__main__":
#     main()

#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


from collections import deque


def find_positions(grid, height, width):
    start_row, start_col = -1, -1
    goal_row, goal_col = -1, -1
    for row in range(height):
        for col in range(width):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col
    return start_row, start_col, goal_row, goal_col


def bfs_shortest_path(height, width, grid, start_row, start_col, goal_row, goal_col):
    distance = [[[-1] * 2 for _ in range(width)] for __ in range(height)]
    queue = deque()

    distance[start_row][start_col][0] = 0
    distance[start_row][start_col][1] = 0
    queue.append((start_row, start_col, 0))
    queue.append((start_row, start_col, 1))

    while queue:
        current_row, current_col, move_type = queue.popleft()

        if current_row == goal_row and current_col == goal_col:
            return distance[current_row][current_col][move_type]

        if move_type == 0:
            directions = [
                (current_row + 1, current_col),
                (current_row - 1, current_col),
            ]
            next_move_type = 1
        else:
            directions = [
                (current_row, current_col + 1),
                (current_row, current_col - 1),
            ]
            next_move_type = 0

        for new_row, new_col in directions:
            if 0 <= new_row < height and 0 <= new_col < width:
                if (
                    grid[new_row][new_col] != "#"
                    and distance[new_row][new_col][next_move_type] == -1
                ):
                    distance[new_row][new_col][next_move_type] = (
                        distance[current_row][current_col][move_type] + 1
                    )
                    queue.append((new_row, new_col, next_move_type))

    return -1


def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    start_row, start_col, goal_row, goal_col = find_positions(grid, H, W)
    min_moves = bfs_shortest_path(H, W, grid, start_row, start_col, goal_row, goal_col)
    print(min_moves)


if __name__ == "__main__":
    main()

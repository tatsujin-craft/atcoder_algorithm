#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def count_safe_squares(N, M, knights):
#     knight_moves = [
#         (2, 1),
#         (1, 2),
#         (-1, 2),
#         (-2, 1),
#         (-2, -1),
#         (-1, -2),
#         (1, -2),
#         (2, -1),
#     ]
#     unsafe_positions = set()

#     for a, b in knights:
#         unsafe_positions.add((a, b))
#         for dx, dy in knight_moves:
#             x, y = a + dx, b + dy
#             if 1 <= x <= N and 1 <= y <= N:
#                 unsafe_positions.add((x, y))

#     total_squares = N * N
#     safe_squares = total_squares - len(unsafe_positions)
#     return safe_squares


# def count_safe_squares(N, M, knights):
#     knight_moves = [
#         (2, 1),
#         (1, 2),
#         (-1, 2),
#         (-2, 1),
#         (-2, -1),
#         (-1, -2),
#         (1, -2),
#         (2, -1),
#     ]
#     attacked_positions = set()

#     for a, b in knights:
#         for dx, dy in knight_moves:
#             x, y = a + dx, b + dy
#             if 1 <= x <= N and 1 <= y <= N:
#                 attacked_positions.add((x, y))

#     total_squares = N * N
#     safe_squares = total_squares - len(attacked_positions) - M
#     return safe_squares


def count_safe_squares(N, M, knights):
    knight_moves = [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]
    attacked_positions = set()
    knight_positions = set(knights)

    for a, b in knights:
        for dx, dy in knight_moves:
            x, y = a + dx, b + dy
            if 1 <= x <= N and 1 <= y <= N and (x, y) not in knight_positions:
                attacked_positions.add((x, y))

    total_squares = N * N
    safe_squares = total_squares - len(attacked_positions) - M
    return safe_squares


def main():
    N, M = map(int, input().split())
    knights = [tuple(map(int, input().split())) for _ in range(M)]
    print(count_safe_squares(N, M, knights))


if __name__ == "__main__":
    main()

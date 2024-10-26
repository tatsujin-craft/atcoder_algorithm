#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def count_safe_positions(board):
    rows, cols = set(), set()
    for i in range(8):
        for j in range(8):
            if board[i][j] == "#":
                rows.add(i)
                cols.add(j)

    safe_count = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == "." and i not in rows and j not in cols:
                safe_count += 1

    return safe_count


def main():
    board = [input() for _ in range(8)]
    safe_positions = count_safe_positions(board)
    print(safe_positions)


if __name__ == "__main__":
    main()

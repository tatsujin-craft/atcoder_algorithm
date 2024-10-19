#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, Q = map(int, input().split())
    commands = [input().split() for _ in range(Q)]

    left = 1
    right = 2
    total_moves = 0

    def calculate_moves(current, target, blocked):
        clockwise = (target - current + N) % N
        counterclockwise = (current - target + N) % N
        if blocked is not None:
            block_clockwise = (blocked - current + N) % N
            block_counterclockwise = (current - blocked + N) % N
            if clockwise >= block_clockwise:
                clockwise = float("inf")
            if counterclockwise >= block_counterclockwise:
                counterclockwise = float("inf")
        return min(clockwise, counterclockwise)

    for hand, target in commands:
        target = int(target)
        if hand == "R":
            moves = calculate_moves(right, target, left)
            total_moves += moves
            right = target
            # Debug log
            # print(f"Move Right to {target}: {moves} moves, Total: {total_moves}")
        else:
            moves = calculate_moves(left, target, right)
            total_moves += moves
            left = target
            # Debug log
            # print(f"Move Left to {target}: {moves} moves, Total: {total_moves}")

    print(total_moves)


if __name__ == "__main__":
    main()

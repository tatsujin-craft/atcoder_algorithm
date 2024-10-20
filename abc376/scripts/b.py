#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def calculate_moves_v1(N, current_position, target_position, blocked_position):
    """
    Modulo-operation version.
    """
    # Calculate moves to target position in CW and CCW
    cw_moves = (target_position - current_position + N) % N
    ccw_moves = (current_position - target_position + N) % N

    # Check blocked route
    if blocked_position is not None:
        # Calculate moves to blocked position in CW and CCW
        cw_moves_to_blocked = (blocked_position - current_position + N) % N
        ccw_moves_to_blocked = (current_position - blocked_position + N) % N
        # Check CW route is blocked (take a detour)
        if cw_moves >= cw_moves_to_blocked:
            cw_moves = float("inf")
        # Check CCW route is blocked (take a detour)
        if ccw_moves >= ccw_moves_to_blocked:
            ccw_moves = float("inf")

    # Get moves to target in CW or CCW with not blocked
    moves_to_target = min(cw_moves, ccw_moves)
    return moves_to_target


def calculate_moves_v2(N, current_position, target_position, blocked_position):
    """
    Reduced branching version.
    Only current < blocked < target, Not multiple branching L<R<T, L<T<R, R<T<L...
    """
    if current_position > target_position:
        # Swap
        current_position, target_position = target_position, current_position

    if current_position < blocked_position < target_position:
        # Move to CCW
        ccw_moves = N + current_position - target_position
        return ccw_moves
    else:
        # Move to CW
        cw_moves = target_position - current_position
        return cw_moves


def main():
    N, Q = map(int, input().split())
    queries = [input().split() for _ in range(Q)]

    prev_left_position = 1
    prev_right_position = 2
    total_moves = 0

    for hand, target_position in queries:
        target_position = int(target_position)
        # Right hand
        if hand == "R":
            moves = calculate_moves_v1(N, prev_right_position, target_position, prev_left_position)
            # moves = calculate_moves_v2(N, prev_right_position, target_position, prev_left_position)
            total_moves += moves
            prev_right_position = target_position
            print(f"Move Right to {target_position}: {moves} moves, Total: {total_moves}")
        # Left hand
        else:
            moves = calculate_moves_v1(N, prev_left_position, target_position, prev_right_position)
            # moves = calculate_moves_v2(N, prev_left_position, target_position, prev_right_position)
            total_moves += moves
            prev_left_position = target_position
            print(f"Move Left to {target_position}: {moves} moves, Total: {total_moves}")

    print(total_moves)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def update_move(pigeon_position, pigeonholes, multi_pigeonholes, P, H):
    old_pigeonhole = pigeon_position[P]
    if pigeonholes[old_pigeonhole] == 2:
        multi_pigeonholes -= 1
    pigeonholes[old_pigeonhole] -= 1

    if pigeonholes[H] == 1:
        multi_pigeonholes += 1
    pigeonholes[H] += 1
    pigeon_position[P] = H

    return multi_pigeonholes


def process_queries(N, Q):
    pigeon_position = [i for i in range(N + 1)]
    pigeonholes = [1] * (N + 1)
    multi_pigeonholes = 0

    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            P = int(query[1])
            H = int(query[2])
            multi_pigeonholes = update_move(
                pigeon_position, pigeonholes, multi_pigeonholes, P, H
            )
        else:
            print(multi_pigeonholes)


def main():
    N, Q = map(int, input().split())

    process_queries(N, Q)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    n, q = map(int, input().split())

    pigeon_indexes = list(range(n + 1))
    nest_indexes = list(range(n + 1))
    nest_positions = list(range(n + 1))

    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            a = int(query[1])
            b = int(query[2])
            pigeon_indexes[a] = nest_positions[b]
        elif query[0] == "2":
            a = int(query[1])
            b = int(query[2])
            i = nest_positions[a]
            j = nest_positions[b]
            nest_indexes[i], nest_indexes[j] = nest_indexes[j], nest_indexes[i]
            nest_positions[a], nest_positions[b] = nest_positions[b], nest_positions[a]
        else:
            a = int(query[1])
            print(nest_indexes[pigeon_indexes[a]])


if __name__ == "__main__":
    main()

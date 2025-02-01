#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def create_thresholds_list(columns, total_columns):
    min_count = min(len(columns[c]) for c in range(1, total_columns + 1))
    thresholds = []
    for r in range(min_count):
        current_max = 0
        for c in range(1, total_columns + 1):
            if columns[c][r] > current_max:
                current_max = columns[c][r]
        thresholds.append(current_max)
    return thresholds


def binary_search_right(thresholds, time_t):
    left = 0
    right = len(thresholds)
    while left < right:
        mid = (left + right) // 2
        if thresholds[mid] <= time_t:
            left = mid + 1
        else:
            right = mid
    return left


def assign_ranks(n, total_columns, blocks):
    col_blocks = [[] for _ in range(total_columns + 1)]
    for i in range(1, n + 1):
        col, y = blocks[i]
        col_blocks[col].append((y, i))
    ranks = [0] * (n + 1)
    for c in range(1, total_columns + 1):
        col_blocks[c].sort(key=lambda pair: pair[0])
        for rank, (_, block_id) in enumerate(col_blocks[c], start=1):
            ranks[block_id] = rank
    return ranks


def main():
    N, W = map(int, input().split())
    columns = [[] for _ in range(W + 1)]
    blocks = [None] * (N + 1)
    for i in range(1, N + 1):
        x, y = map(int, input().split())
        columns[x].append(y)
        blocks[i] = (x, y)
    for c in range(1, W + 1):
        columns[c].sort()

    Q = int(input())
    queries = []
    for _ in range(Q):
        t, a = map(int, input().split())
        queries.append((t, a))

    thresholds = create_thresholds_list(columns, W)
    ranks = assign_ranks(N, W, blocks)

    # Process queries
    results = []
    for t, a in queries:
        cleared = binary_search_right(thresholds, t)
        if ranks[a] > cleared:
            results.append("Yes")
        else:
            results.append("No")

    print("\n".join(results))


if __name__ == "__main__":
    main()

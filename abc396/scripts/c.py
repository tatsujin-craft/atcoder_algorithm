#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_max_total_value(n, blacks, whites):
    # Black balls
    blacks.sort(reverse=True)
    prefix_black = [0] * (n + 1)
    for i in range(n):
        prefix_black[i + 1] = prefix_black[i] + blacks[i]
    cnt_nonneg = 0

    for b in blacks:
        if b >= 0:
            cnt_nonneg += 1
        else:
            break

    # White balls
    white_pos = [w for w in whites if w > 0]
    white_pos.sort(reverse=True)
    k = len(white_pos)
    prefix_white = [0] * (k + 1)
    for i in range(k):
        prefix_white[i + 1] = prefix_white[i] + white_pos[i]

    # Total value
    total_value = prefix_black[cnt_nonneg]
    for x in range(1, min(k, n) + 1):
        if x <= cnt_nonneg:
            black_sum = prefix_black[cnt_nonneg]
        else:
            if x <= n:
                black_sum = prefix_black[x]
            else:
                continue
        candidate = prefix_white[x] + black_sum
        if candidate > total_value:
            total_value = candidate

    max_total_value = max(total_value, 0)
    return max_total_value


def main():
    n, m = map(int, input().split())
    blacks = list(map(int, input().split()))
    whites = list(map(int, input().split()))

    result = get_max_total_value(n, blacks, whites)
    print(result)


if __name__ == "__main__":
    main()

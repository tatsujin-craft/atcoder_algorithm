#!/usr/bin/env python3
"""
Script Name: a.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, C = map(int, input().split())
    T = list(map(int, input().split()))
    # print(T)

    prev_time = T[0]
    count = 1
    for i in range(N):
        diff_time = T[i] - prev_time
        # print("diff", diff_time)
        if diff_time >= C:
            count += 1
            prev_time = T[i]
            # print("count", count, "prev", prev_time)

    print(count)


if __name__ == "__main__":
    main()

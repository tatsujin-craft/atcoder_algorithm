#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_result_string(N, K, S):
    blocks = []
    i = 0
    while i < N:
        if S[i] == "1":
            start = i
            while i < N and S[i] == "1":
                i += 1
            blocks.append((start, i))
        else:
            i += 1

    left_block = blocks[K - 2]
    target_block = blocks[K - 1]

    result_string = (
        S[: left_block[1]]
        + S[target_block[0] : target_block[1]]
        + S[left_block[1] : target_block[0]]
        + S[target_block[1] :]
    )
    return result_string


def main():
    N, K = map(int, input().split())
    S = input()

    result_string = get_result_string(N, K, S)
    print(result_string)


if __name__ == "__main__":
    main()

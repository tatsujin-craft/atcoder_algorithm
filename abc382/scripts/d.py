#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def backtrack(N, M, seq, k, sequences):
    if k == N:
        sequences.append(seq.copy())
        return
    if k == 0:
        lower = 1
    else:
        lower = seq[-1] + 10
    upper = M - 10 * (N - k - 1)
    for num in range(lower, upper + 1):
        seq.append(num)
        backtrack(N, M, seq, k + 1, sequences)
        seq.pop()


def main():
    N, M = map(int, input().split())
    sequences = []

    backtrack(N, M, [], 0, sequences)

    print(len(sequences))
    for seq in sequences:
        print(" ".join(map(str, seq)))


if __name__ == "__main__":
    main()

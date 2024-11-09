#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def count_moves_v1(N, M, X, A):
    stones = [(X[i] - 1, A[i]) for i in range(M)]
    stones.sort()

    moves = 0
    extra = 0
    index = 0

    for pos in range(N):
        if index < M and stones[index][0] == pos:
            count = stones[index][1] + extra
            index += 1
        else:
            count = extra

        if count > 1:
            extra = count - 1
            moves += count - 1
        elif count == 1:
            extra = 0
        else:
            return -1

    return moves if extra == 0 else -1


def count_moves_v2(N, M, X, A):
    stones = [(X[i] - 1, A[i]) for i in range(M)]
    stones.sort()
    moves = 0
    extra = 0
    index = 0

    for pos in range(N):
        if index < M and stones[index][0] == pos:
            count = stones[index][1] + extra
            index += 1
        else:
            count = extra

        if count > 1:
            extra = count - 1
            moves += count - 1
        elif count == 1:
            extra = 0
        else:
            return -1

    if extra == 0:
        return moves
    else:
        return -1


def count_moves_v3(N, M, X, A):
    stones = {}
    for i in range(M):
        stones[X[i] - 1] = A[i]

    moves = 0
    extra = 0

    for i in range(N):
        count = stones.get(i, 0) + extra
        if count > 1:
            moves += count - 1
            extra = count - 1
        elif count == 1:
            extra = 0
        else:
            return -1

    return moves if extra == 0 else -1


def count_moves(N, M, X, A):
    stones = sorted((X[i] - 1, A[i]) for i in range(M))
    sum_stones = 0
    sum_idx = 0

    for pos, count in stones:
        if sum_stones < pos:
            return -1

        sum_stones += count
        sum_idx += count * (pos + 1)

    if sum_stones != N:
        return -1

    return N * (N + 1) // 2 - sum_idx


def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    A = list(map(int, input().split()))

    result = count_moves_v1(N, M, X, A)
    print(result)

    result = count_moves_v2(N, M, X, A)
    print(result)

    result = count_moves_v3(N, M, X, A)
    print(result)

    result = count_moves(N, M, X, A)
    print(result)


if __name__ == "__main__":
    main()

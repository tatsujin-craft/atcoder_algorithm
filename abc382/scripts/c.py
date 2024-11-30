#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    tree = [0] * (4 * N)

    def build(v, l, r):
        if l == r:
            tree[v] = A[l]
        else:
            mid = (l + r) // 2
            build(2 * v, l, mid)
            build(2 * v + 1, mid + 1, r)
            tree[v] = min(tree[2 * v], tree[2 * v + 1])

    def query(v, l, r, B_val):
        if tree[v] > B_val:
            return -1
        if l == r:
            return l + 1
        mid = (l + r) // 2
        if tree[2 * v] <= B_val:
            return query(2 * v, l, mid, B_val)
        else:
            return query(2 * v + 1, mid + 1, r, B_val)

    build(1, 0, N - 1)

    res = []
    for b in B:
        ans = query(1, 0, N - 1, b)
        res.append(str(ans) if ans != -1 else "-1")

    print("\n".join(res))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

from collections import deque


def find_min_restricted_sum_seq(n, xyz_seq_tuple):
    graph = [[] for _ in range(n)]
    for x, y, z in xyz_seq_tuple:
        graph[x - 1].append((y - 1, z))
        graph[y - 1].append((x - 1, z))
    d = [None] * n
    min_restricted_sum_seq = [None] * n

    for i in range(n):
        if d[i] is None:
            comp = []
            dq = deque([i])
            d[i] = 0
            while dq:
                u = dq.popleft()
                comp.append(u)
                for v, z in graph[u]:
                    if d[v] is None:
                        d[v] = d[u] ^ z
                        dq.append(v)
                    elif d[v] != d[u] ^ z:
                        return None
            comp_size = len(comp)
            offset = 0
            for b in range(31):
                cnt = 0
                for u in comp:
                    if d[u] & (1 << b):
                        cnt += 1
                if cnt > comp_size - cnt:
                    offset |= 1 << b
            for u in comp:
                min_restricted_sum_seq[u] = offset ^ d[u]
    return min_restricted_sum_seq


def main():
    n, m = map(int, input().split())
    xyz_seq_tuple = [tuple(map(int, input().split())) for _ in range(m)]

    result_seq = find_min_restricted_sum_seq(n, xyz_seq_tuple)
    if result_seq is None:
        print(-1)
    else:
        print(" ".join(map(str, result_seq)))


if __name__ == "__main__":
    main()

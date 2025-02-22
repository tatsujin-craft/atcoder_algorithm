#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

from collections import deque

INF = 10**9


def get_shortest_paths_by_bfs(n, graph):
    out_edges = [[] for _ in range(n)]
    in_edges = [[] for _ in range(n)]
    for i in range(n):
        row = graph[i]
        for j in range(n):
            c = row[j]
            if c != "-":
                out_edges[i].append((j, c))
                in_edges[j].append((i, c))

    sp = [[INF] * n for _ in range(n)]
    dq = deque()

    for i in range(n):
        sp[i][i] = 0
        dq.append((i, i, 0))

    for i in range(n):
        for j, c in out_edges[i]:
            if sp[i][j] > 1:
                sp[i][j] = 1
                dq.append((i, j, 1))

    while dq:
        i, j, d = dq.popleft()
        if d != sp[i][j]:
            continue
        in_edges_i = in_edges[i]
        out_edges_j = out_edges[j]
        for u, c1 in in_edges_i:
            for v, c2 in out_edges_j:
                if c1 == c2:
                    nd = d + 2
                    if nd < sp[u][v]:
                        sp[u][v] = nd
                        dq.append((u, v, nd))
    return sp


def print_result(sp, n):
    for i in range(n):
        line_parts = []
        for j in range(n):
            if sp[i][j] == INF:
                line_parts.append("-1")
            else:
                line_parts.append(str(sp[i][j]))
        print(" ".join(line_parts))


def main():
    n = int(input())
    graph = [input() for _ in range(n)]

    sp = get_shortest_paths_by_bfs(n, graph)
    print_result(sp, n)


if __name__ == "__main__":
    main()

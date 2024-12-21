#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def dfs(u, parent, adj, leaves, children_leaves):
    is_leaf = True
    total_leaves = 0
    for v in adj[u]:
        if v != parent:
            is_leaf = False
            dfs(v, u, adj, leaves, children_leaves)
            children_leaves[u].append(leaves[v])
            total_leaves += leaves[v]
    if is_leaf:
        leaves[u] = 1
    else:
        leaves[u] = total_leaves


def main():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    leaves = [0] * (N + 1)
    children_leaves = [[] for _ in range(N + 1)]
    dfs(1, -1, adj, leaves, children_leaves)

    max_keep = 0
    for u in range(1, N + 1):
        cl = sorted(children_leaves[u], reverse=True)
        if not cl:
            continue
        max_y = cl[0]
        x = 0
        for y in range(1, max_y + 1):
            while x < len(cl) and cl[x] >= y:
                x += 1
            keep = 1 + x + x * y
            if keep > max_keep:
                max_keep = keep
    print(abs(N - max_keep))


if __name__ == "__main__":
    main()

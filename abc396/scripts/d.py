#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def find_min_xor_path(n, graph):
    INF = 1 << 62
    dp = [[set() for _ in range(n)] for _ in range(1 << n)]
    dp[1 << 0][0].add(0)
    for mask in range(1 << n):
        for v in range(n):
            for cost in dp[mask][v]:
                for nv, w in graph[v]:
                    if mask & (1 << nv):
                        continue
                    new_mask = mask | (1 << nv)
                    new_cost = cost ^ w
                    dp[new_mask][nv].add(new_cost)
    min_xor_cost = INF
    for mask in range(1 << n):
        if mask & (1 << (n - 1)):
            if dp[mask][n - 1]:
                min_xor_cost = min(min_xor_cost, min(dp[mask][n - 1]))
    return min_xor_cost


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))

    result = find_min_xor_path(n, graph)
    print(result)


if __name__ == "__main__":
    main()

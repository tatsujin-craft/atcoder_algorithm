#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


import heapq


def get_min_cost_by_dijkstra(n, x, g0, g1):
    INF = float("inf")
    dist = [[INF, INF] for _ in range(n + 1)]
    dist[1][0] = 0
    pq = [(0, 1, 0)]

    while pq:
        d, u, s = heapq.heappop(pq)
        if d != dist[u][s]:
            continue
        if u == n:
            return d
        if s == 0:
            for v in g0[u]:
                nd = d + 1
                if nd < dist[v][0]:
                    dist[v][0] = nd
                    heapq.heappush(pq, (nd, v, 0))
        else:
            for v in g1[u]:
                nd = d + 1
                if nd < dist[v][1]:
                    dist[v][1] = nd
                    heapq.heappush(pq, (nd, v, 1))
        ns = 1 - s
        nd = d + x
        if nd < dist[u][ns]:
            dist[u][ns] = nd
            heapq.heappush(pq, (nd, u, ns))
    return -1


def main():
    n, m, x = map(int, input().split())
    original_graph = [[] for _ in range(n + 1)]
    reversed_graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        original_graph[u].append(v)
        reversed_graph[v].append(u)

    min_cost = get_min_cost_by_dijkstra(n, x, original_graph, reversed_graph)
    print(min_cost)


if __name__ == "__main__":
    main()

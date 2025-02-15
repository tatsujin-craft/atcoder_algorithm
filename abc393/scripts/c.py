#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def find_remove_edges(edges):
    freq = {}
    loops = 0
    for u, v in edges:
        if u == v:
            loops += 1
        else:
            if u > v:
                u, v = v, u
            if (u, v) not in freq:
                freq[(u, v)] = 0
            freq[(u, v)] += 1

    remove_edges = loops
    for c in freq.values():
        remove_edges += c - 1

    return remove_edges


def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))

    result = find_remove_edges(edges)
    print(result)


if __name__ == "__main__":
    main()

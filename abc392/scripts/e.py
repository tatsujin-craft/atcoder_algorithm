#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return root_x
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return root_x


def reconnect_cables(n, uf, unused_cables):
    connected_components = []
    for i in range(n):
        root = uf.find(i)
        if root == i:
            connected_components.append((len(unused_cables[root]), root))

    connected_components.sort(key=lambda x: x[0], reverse=True)

    component_count = len(connected_components)
    print(component_count - 1)

    if component_count <= 1:
        return

    next_component_index = 1
    for _, root in connected_components:
        for server_a, server_b, cable_id in unused_cables[root]:
            if next_component_index < component_count:
                print(
                    cable_id + 1,
                    server_a + 1,
                    connected_components[next_component_index][1] + 1,
                )
                next_component_index += 1
            else:
                break
        if next_component_index >= component_count:
            break


def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    unused_cables = [[] for _ in range(N)]

    for cable_id in range(M):
        server_a, server_b = map(int, input().split())
        server_a -= 1
        server_b -= 1
        if uf.same(server_a, server_b):
            unused_cables[uf.find(server_a)].append((server_a, server_b, cable_id))
        else:
            uf.unite(server_a, server_b)

    reconnect_cables(N, uf, unused_cables)


if __name__ == "__main__":
    main()

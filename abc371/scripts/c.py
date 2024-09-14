#!/usr/bin/env python3


import sys
import itertools


# def parse_input():
#     # 標準入力からデータを読み取ります
#     input = sys.stdin.read
#     data = input().splitlines()

#     # グラフ G と H の頂点数と辺の数を読み取る
#     N = int(data[0].strip())
#     Mg = int(data[1].strip())

#     # グラフ G の辺を読み取る
#     edges_g = set()
#     for i in range(2, 2 + Mg):
#         u, v = map(int, data[i].strip().split())
#         edges_g.add((min(u, v), max(u, v)))

#     # グラフ H の辺を読み取る
#     Mh = int(data[2 + Mg].strip())
#     edges_h = set()
#     for i in range(3 + Mg, 3 + Mg + Mh):
#         u, v = map(int, data[i].strip().split())
#         edges_h.add((min(u, v), max(u, v)))

#     # Aijのコストを読み取る
#     A = []
#     current_line = 3 + Mg + Mh
#     for i in range(N - 1):
#         A.append(list(map(int, data[current_line].strip().split())))
#         current_line += 1

#     return N, edges_g, edges_h, A


# def calculate_minimum_cost(N, edges_g, edges_h, A):
#     # グラフ G と H の各辺のセット差分を計算する
#     edges_to_add = edges_h - edges_g
#     edges_to_remove = edges_g - edges_h

#     # 最小コストを求める
#     min_cost = 0

#     # 追加するためのコストを計算
#     for u, v in edges_to_add:
#         u, v = u - 1, v - 1  # インデックスを0ベースに変換
#         if u > v:
#             u, v = v, u
#         min_cost += A[u][v - u - 1]

#     # 削除するためのコストを計算
#     for u, v in edges_to_remove:
#         u, v = u - 1, v - 1  # インデックスを0ベースに変換
#         if u > v:
#             u, v = v, u
#         min_cost += A[u][v - u - 1]

#     return min_cost


# def main():
#     N, edges_g, edges_h, A = parse_input()
#     min_cost = calculate_minimum_cost(N, edges_g, edges_h, A)
#     print(min_cost)


# if __name__ == "__main__":
#     main()


def parse_input():
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0].strip())
    Mg = int(data[1].strip())

    # Initialize adjacency matrix for G and H
    G = [[0] * N for _ in range(N)]
    H = [[0] * N for _ in range(N)]

    # Read edges for graph G
    for i in range(2, 2 + Mg):
        u, v = map(int, data[i].strip().split())
        G[u - 1][v - 1] = 1
        G[v - 1][u - 1] = 1

    Mh = int(data[2 + Mg].strip())

    # Read edges for graph H
    for i in range(3 + Mg, 3 + Mg + Mh):
        u, v = map(int, data[i].strip().split())
        H[u - 1][v - 1] = 1
        H[v - 1][u - 1] = 1

    # Read the cost matrix A
    A = []
    current_line = 3 + Mg + Mh
    for i in range(N - 1):
        A.append(list(map(int, data[current_line].strip().split())))
        current_line += 1

    return N, G, H, A


def calculate_minimum_cost(N, G, H, A):
    # Initialize dp table for the minimum cost to convert G to H
    dp = [[float("inf")] * (1 << (N * (N - 1) // 2)) for _ in range(2)]
    dp[0][0] = 0

    edges = [(i, j) for i in range(N) for j in range(i + 1, N)]
    total_edges = len(edges)

    # Iterate through all subsets of edges
    for mask in range(1 << total_edges):
        cost = 0
        for idx, (u, v) in enumerate(edges):
            if mask & (1 << idx):
                if G[u][v] != H[u][v]:
                    cost += A[min(u, v)][abs(u - v) - 1]
            else:
                if G[u][v] == H[u][v]:
                    cost += A[min(u, v)][abs(u - v) - 1]
        dp[1][mask] = min(dp[1][mask], cost)

    return min(dp[1])


def main():
    N, G, H, A = parse_input()
    min_cost = calculate_minimum_cost(N, G, H, A)
    print(min_cost)


if __name__ == "__main__":
    main()

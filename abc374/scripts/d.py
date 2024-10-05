#!/usr/bin/env python3

import itertools
import math

# TOLERANCE = 1e-6


# def calculate_distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# def calculate_min_time(N, S, T, segments):
#     min_time = float("inf")

#     for perm in itertools.permutations(range(N)):
#         time = 0.0
#         x, y = 0, 0

#         for i in perm:
#             A, B, C, D = segments[i]
#             move_time = calculate_distance(x, y, A, B) / S
#             time += move_time

#             print_time = calculate_distance(A, B, C, D) / T
#             time += print_time

#             x, y = C, D

#         if time < min_time - TOLERANCE:
#             min_time = time
#             # print(f"New minimum time found: {min_time:.20f} for permutation {perm}")

#     return min_time


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calculate_min_time(N, S, T, segments):
    min_time = float("inf")

    perm = list(itertools.permutations(range(N)))  # 全順列を生成
    for p in perm:
        for i in range(1 << N):  # 各向きについて全探索
            current_time = 0.0
            cur_position = (0, 0)  # 初期位置 (0, 0)

            for j in range(N):
                el = p[j]
                start_point = segments[el][0]  # (A, B)
                end_point = segments[el][1]  # (C, D)

                if i & (1 << j):  # ビットが1ならば逆方向
                    current_time += dist(cur_position, start_point) / S
                    current_time += dist(start_point, end_point) / T
                    cur_position = end_point
                else:  # ビットが0ならば順方向
                    current_time += dist(cur_position, end_point) / S
                    current_time += dist(end_point, start_point) / T
                    cur_position = start_point

            min_time = min(min_time, current_time)

    return min_time


def main():
    N, S, T = map(int, input().split())
    segments = []
    for _ in range(N):
        A, B, C, D = map(int, input().split())
        # segments.append((A, B, C, D))
        segments.append(((A, B), (C, D)))  # (A, B) -> (C, D)

    min_time = calculate_min_time(N, S, T, segments)
    print(f"{min_time:.12f}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def main():
#     N, M = map(int, input().split())
#     max_b_row = {}
#     min_w_row = {}
#     max_b_col = {}
#     min_w_col = {}

#     for _ in range(M):
#         x, y, c = input().split()
#         x = int(x)
#         y = int(y)
#         if c == "B":
#             if x in max_b_row:
#                 max_b_row[x] = max(max_b_row[x], y)
#             else:
#                 max_b_row[x] = y
#             if y in max_b_col:
#                 max_b_col[y] = max(max_b_col[y], x)
#             else:
#                 max_b_col[y] = x
#         else:
#             if x in min_w_row:
#                 min_w_row[x] = min(min_w_row[x], y)
#             else:
#                 min_w_row[x] = y
#             if y in min_w_col:
#                 min_w_col[y] = min(min_w_col[y], x)
#             else:
#                 min_w_col[y] = x

#     for x in set(list(max_b_row.keys()) + list(min_w_row.keys())):
#         max_b = max_b_row.get(x, 0)
#         min_w = min_w_row.get(x, N + 1)
#         if max_b > min_w - 1:
#             print("No")
#             return
#     for y in set(list(max_b_col.keys()) + list(min_w_col.keys())):
#         max_b = max_b_col.get(y, 0)
#         min_w = min_w_col.get(y, N + 1)
#         if max_b > min_w - 1:
#             print("No")
#             return
#     print("Yes")


def main():
    N, M = map(int, input().split())
    black_cells = []
    white_cells = []
    for _ in range(M):
        x, y, c = input().split()
        x = int(x)
        y = int(y)
        if c == "B":
            black_cells.append((x, y))
        else:
            white_cells.append((x, y))

    i_min = 0
    for x, y in black_cells:
        i_min = max(i_min, max(x, y))

    i_max = N
    for x, y in white_cells:
        i_max = min(i_max, min(x, y) - 1)
        if i_max < 0:
            break

    if i_min <= i_max:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

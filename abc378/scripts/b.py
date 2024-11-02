#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def main():
#     N = int(input())
#     rules = [tuple(map(int, input().split())) for _ in range(N)]
#     Q = int(input())
#     queries = [tuple(map(int, input().split())) for _ in range(Q)]

#     for t, d in queries:
#         q, r = rules[t - 1]
#         day = d
#         while day % q != r:
#             day += 1
#         print(day)


# from bisect import bisect_left


# def main():
#     N = int(input())
#     rules = [tuple(map(int, input().split())) for _ in range(N)]
#     Q = int(input())
#     queries = [tuple(map(int, input().split())) for _ in range(Q)]

#     collection_days = {}
#     for idx, (q, r) in enumerate(rules):
#         days = []
#         for i in range(r, 10001, q):
#             days.append(i)
#         collection_days[idx + 1] = days

#     for t, d in queries:
#         days = collection_days[t]
#         pos = bisect_left(days, d)
#         print(days[pos])


# if __name__ == "__main__":
#     main()


def main():
    N = int(input())
    rules = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(Q)]

    for t, d in queries:
        q, r = rules[t - 1]
        day = d + (q - (d % q) + r) % q
        print(day)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


# def village_population_in_range(n, x, p, queries):
#     villages = sorted(zip(x, p))
#     results = []

#     for l, r in queries:
#         total_population = 0
#         for xi, pi in villages:
#             if l <= xi <= r:
#                 total_population += pi
#         results.append(total_population)

#     return results


# def main():
#     n = int(input())
#     x = list(map(int, input().split()))
#     p = list(map(int, input().split()))
#     q = int(input())
#     queries = [tuple(map(int, input().split())) for _ in range(q)]

#     result = village_population_in_range(n, x, p, queries)

#     for res in result:
#         print(res)

from bisect import bisect_left, bisect_right


def village_population_in_range(n, x, p, queries):
    villages = sorted(zip(x, p))
    sorted_x, sorted_p = zip(*villages)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + sorted_p[i - 1]

    results = []

    for l, r in queries:
        left_index = bisect_left(sorted_x, l)
        right_index = bisect_right(sorted_x, r) - 1

        if left_index <= right_index:
            total_population = prefix_sum[right_index + 1] - prefix_sum[left_index]
        else:
            total_population = 0

        results.append(total_population)

    return results


def main():
    n = int(input())
    x = list(map(int, input().split()))
    p = list(map(int, input().split()))
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    result = village_population_in_range(n, x, p, queries)

    for res in result:
        print(res)


if __name__ == "__main__":
    main()

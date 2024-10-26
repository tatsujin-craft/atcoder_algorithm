#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

from bisect import bisect_left


def count_by_brute_force(M, intervals):
    count = 0
    for l in range(1, M + 1):
        for r in range(l, M + 1):
            include_all = False
            for L, R in intervals:
                if L >= l and R <= r:
                    include_all = True
                    break
            if not include_all:
                count += 1
    return count


def count_by_interval_scheduling(M, intervals):
    intervals.sort()
    end_points = sorted(R for _, R in intervals)
    count = 0

    for l in range(1, M + 1):
        r_idx = bisect_left(end_points, l)
        temp_count = 0
        for r in range(l, M + 1):
            include_all = False
            for L, R in intervals:
                if L >= l and R <= r:
                    include_all = True
                    break
            if not include_all:
                temp_count += 1
        # print(f"l: {l}, Possible r-count: {temp_count}")
        count += temp_count

    return count


def count_by_optimized_interval(M, intervals):
    coverage = [0] * (M + 2)

    for L, R in intervals:
        coverage[L] += 1
        if R + 1 <= M:
            coverage[R + 1] -= 1

    for i in range(1, M + 1):
        coverage[i] += coverage[i - 1]

    valid_count = [0] * (M + 1)
    for i in range(1, M + 1):
        if coverage[i] == 0:
            valid_count[i] = valid_count[i - 1] + 1
        else:
            valid_count[i] = valid_count[i - 1]

    valid_combinations = 0
    for l in range(1, M + 1):
        valid_combinations += valid_count[M] - valid_count[l - 1]

    return valid_combinations


class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (2 * size)

    def add(self, idx, value):
        idx += self.size
        self.tree[idx] += value
        while idx > 1:
            idx //= 2
            self.tree[idx] = self.tree[2 * idx] + self.tree[2 * idx + 1]

    def query(self, left, right):
        result = 0
        left += self.size
        right += self.size
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result


def count_by_segment_tree(M, intervals):
    seg_tree = SegmentTree(M + 1)

    for L, R in intervals:
        seg_tree.add(L, 1)
        if R + 1 <= M:
            seg_tree.add(R + 1, -1)

    valid_combinations = 0
    current_coverage = 0

    for l in range(1, M + 1):
        current_coverage += seg_tree.query(l, l + 1)
        if current_coverage == 0:
            valid_combinations += M - l + 1

    return valid_combinations


def count_by_efficient_algorithm(M, intervals):
    d = [1] * (M + 1)

    # 各区間の右端 R に対して、d[R] を更新
    for L, R in intervals:
        d[R] = max(d[R], L + 1)

    # d の累積的更新
    for r in range(1, M + 1):
        d[r] = max(d[r], d[r - 1])

    # 条件を満たす (l, r) の組み合わせの数を計算
    valid_combinations = 0
    for r in range(1, M + 1):
        valid_combinations += r - d[r] + 1

    return valid_combinations


def main():
    N, M = map(int, input().split())
    intervals = [tuple(map(int, input().split())) for _ in range(N)]

    count = count_by_brute_force(M, intervals)
    print("Brute: ", count)

    count = count_by_interval_scheduling(M, intervals)
    print("Interval: ", count)

    count = count_by_optimized_interval(M, intervals)
    print("Optimized Interval: ", count)

    count = count_by_segment_tree(M, intervals)
    print("Segment Tree Interval:", count)

    count = count_by_efficient_algorithm(M, intervals)
    print("Efficient Algorithm Interval:", count)


if __name__ == "__main__":
    main()

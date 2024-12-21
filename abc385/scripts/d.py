#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

import bisect
from collections import defaultdict


def create_segments(commands, Sx, Sy):
    vertical_segments = defaultdict(list)
    horizontal_segments = defaultdict(list)
    cx, cy = Sx, Sy

    for D, C in commands:
        if D == "U":
            nx, ny = cx, cy + C
            vertical_segments[cx].append((min(cy, ny), max(cy, ny)))
        elif D == "D":
            nx, ny = cx, cy - C
            vertical_segments[cx].append((min(cy, ny), max(cy, ny)))
        elif D == "L":
            nx, ny = cx - C, cy
            horizontal_segments[cy].append((min(cx, nx), max(cx, nx)))
        elif D == "R":
            nx, ny = cx + C, cy
            horizontal_segments[cy].append((min(cx, nx), max(cx, nx)))
        cx, cy = nx, ny

    final_x, final_y = cx, cy
    return vertical_segments, horizontal_segments, final_x, final_y


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_start, last_end = merged[-1]
        current_start, current_end = current
        if current_start <= last_end:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append(current)
    return merged


def process_segments(vertical_segments, horizontal_segments):
    for x in vertical_segments:
        vertical_segments[x] = merge_intervals(vertical_segments[x])
    for y in horizontal_segments:
        horizontal_segments[y] = merge_intervals(horizontal_segments[y])
    return vertical_segments, horizontal_segments


def count_passed_houses(houses, vertical_segments, horizontal_segments):
    passed_houses = 0
    for x, y in houses:
        found = False
        if x in vertical_segments:
            intervals = vertical_segments[x]
            pos = bisect.bisect_right(intervals, (y, float("inf"))) - 1
            if pos >= 0 and intervals[pos][0] <= y <= intervals[pos][1]:
                found = True
        if not found and y in horizontal_segments:
            intervals = horizontal_segments[y]
            pos = bisect.bisect_right(intervals, (x, float("inf"))) - 1
            if pos >= 0 and intervals[pos][0] <= x <= intervals[pos][1]:
                found = True
        if found:
            passed_houses += 1

    return passed_houses


def main():
    N, M, Sx, Sy = map(int, input().split())
    houses = [tuple(map(int, input().split())) for _ in range(N)]
    commands = [tuple(input().split()) for _ in range(M)]
    commands = [(D, int(C)) for D, C in commands]

    vertical_segments, horizontal_segments, final_x, final_y = create_segments(
        commands, Sx, Sy
    )
    vertical_segments, horizontal_segments = process_segments(
        vertical_segments, horizontal_segments
    )

    passed_houses = count_passed_houses(houses, vertical_segments, horizontal_segments)
    print(final_x, final_y, passed_houses)


if __name__ == "__main__":
    main()

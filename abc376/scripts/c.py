#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def is_all_toys_fit_in_boxes(x, toy_sizes, box_sizes, N):
    box_sizes_with_new = box_sizes + [x]
    # Sort in descending order
    box_sizes_with_new.sort(reverse=True)
    sorted_toy_sizes = sorted(toy_sizes, reverse=True)
    print(f"Try x={x}, Sorted toy sizes {sorted_toy_sizes}, Sorted box sizes {box_sizes_with_new}")

    # Check all toys fit in boxes
    for i in range(N):
        if sorted_toy_sizes[i] > box_sizes_with_new[i]:
            print(
                f"Toy{i+1} failed. "
                f"Toy size={sorted_toy_sizes[i]}, Box size={box_sizes_with_new[i]}"
            )
            return False
    return True


def main():
    N = int(input())
    toy_sizes = list(map(int, input().split()))
    box_sizes = list(map(int, input().split()))

    low, high = 1, max(toy_sizes)
    print(f"Start binray search")
    print(f"Initial value: low={low}, high={high}\n")

    # Binary search until low == high, and get box size x
    while low < high:
        mid = (low + high) // 2
        print(f"low={low}, Mid={mid}, high={high}")
        if is_all_toys_fit_in_boxes(mid, toy_sizes, box_sizes, N):
            high = mid
            print(f"x={mid} is OK, updating high={high}\n")
        else:
            low = mid + 1
            print(f"x={mid} is too small, updating low={low}\n")

    if is_all_toys_fit_in_boxes(low, toy_sizes, box_sizes, N):
        result = low
        print(f"Min additional box size: x={result}\n")
    else:
        result = -1
        print(f"No result: x={result}\n")

    print(result)


if __name__ == "__main__":
    main()

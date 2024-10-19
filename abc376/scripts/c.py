#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def check_all_toys(x, A, B, N):
    B_with_new_box = B + [x]
    B_with_new_box.sort(reverse=True)
    A_sorted = sorted(A, reverse=True)
    # print(
    #     f"Checking with new box size {x}: Sorted toy sizes {A_sorted}, Sorted box sizes {B_with_new_box}"
    # )
    for i in range(N):
        if A_sorted[i] > B_with_new_box[i]:
            # print(
            #     f"Toy {i+1} with size {A_sorted[i]} does not fit in box {B_with_new_box[i]}"
            # )
            return False
    return True


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    low, high = 1, max(A)
    # print(f"Initial range for x: low={low}, high={high}")

    while low < high:
        mid = (low + high) // 2
        # print(f"Trying mid = {mid}")
        if check_all_toys(mid, A, B, N):
            high = mid
            # print(f"Found valid x = {mid}, updating high to {high}")
        else:
            low = mid + 1
            # print(f"x = {mid} is too small, updating low to {low}")

    result = low if check_all_toys(low, A, B, N) else -1
    # print(f"Final result: {result}")
    print(result)


if __name__ == "__main__":
    main()

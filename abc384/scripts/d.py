#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def find_subsequence_sum(A, X):
    N = len(A)
    B = A + A
    left = 0
    current_sum = 0

    for right in range(2 * N):
        current_sum += B[right]
        while current_sum > X and left <= right:
            current_sum -= B[left]
            left += 1
        if current_sum == X and (right - left + 1) <= N:
            return True
    return False


def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    if sum_A == 0:
        if S == 0:
            print("Yes")
        else:
            print("No")
        return
    if S == 0:
        print("No")
        return

    remainder = S % sum_A
    if remainder == 0:
        if S >= sum_A:
            print("Yes")
        else:
            if find_subsequence_sum(A, S):
                print("Yes")
            else:
                print("No")
    else:
        if find_subsequence_sum(A, remainder):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

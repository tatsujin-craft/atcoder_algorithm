#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

# def count_palindromic_triplets(S):
#     n = len(S)
#     count = 0
#     for i in range(n - 2):
#         for j in range(i + 1, n - 1):
#             for k in range(j + 1, n):
#                 if S[i] == S[k]:
#                     count += 1
#     return count


def count_palindromic_triplets(S):
    length = len(S)
    sum_counts = [[0] * (length + 1) for _ in range(26)]
    print(sum_counts, "\n")

    for i in range(length):
        for j in range(26):
            sum_counts[j][i + 1] = sum_counts[j][i]
        sum_counts[ord(S[i]) - ord("A")][i + 1] += 1
    print(sum_counts, "\n")

    ans = 0
    for i in range(1, length - 1):
        for j in range(26):
            left_count = sum_counts[j][i]
            right_count = sum_counts[j][length] - sum_counts[j][i + 1]
            ans += left_count * right_count
        print(f"ans: {ans}")

    return ans


def main():
    S = input()
    print(S)

    count = count_palindromic_triplets(S)
    print(count)


if __name__ == "__main__":
    main()

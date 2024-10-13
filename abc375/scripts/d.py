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
#     right_count = [0] * 26

#     for c in S:
#         right_count[ord(c) - ord("A")] += 1

#     left_count = [0] * 26

#     for j in range(n):
#         right_count[ord(S[j]) - ord("A")] -= 1
#         for i in range(26):
#             if S[j] != chr(i + ord("A")):
#                 count += left_count[i] * right_count[i]
#         left_count[ord(S[j]) - ord("A")] += 1

#     return count


# def count_palindromic_triplets(S):
#     n = len(S)
#     count = 0
#     left_count = [[0] * 26 for _ in range(n)]
#     right_count = [0] * 26

#     for i in range(1, n):
#         for c in range(26):
#             left_count[i][c] = left_count[i - 1][c]
#         left_count[i][ord(S[i - 1]) - ord("A")] += 1

#     for k in range(n - 1, 1, -1):
#         right_count[ord(S[k]) - ord("A")] += 1
#         for j in range(k - 1, 0, -1):
#             if S[j] == S[k]:
#                 count += left_count[j][ord(S[k]) - ord("A")]

#     return count


# def count_palindromic_triplets(S):
#     n = len(S)
#     count = 0
#     left_count = [[0] * 26 for _ in range(n)]
#     right_count = [0] * 26

#     # Left count initialization
#     for i in range(1, n):
#         for c in range(26):
#             left_count[i][c] = left_count[i - 1][c]
#         left_count[i][ord(S[i - 1]) - ord("A")] += 1

#     # Debug: print left_count table
#     print("Left count table:")
#     for i in range(1, n):
#         print(f"left_count[{i}] = {left_count[i]}")

#     # Right count and calculation
#     for k in range(n - 1, 1, -1):
#         right_count[ord(S[k]) - ord("A")] += 1
#         print(f"\nProcessing for k = {k}, S[k] = {S[k]}")
#         for j in range(k - 1, 0, -1):
#             if S[j] == S[k]:
#                 triplet_count = left_count[j][ord(S[k]) - ord("A")]
#                 count += triplet_count
#                 print(
#                     f"  Match found at j = {j}, S[j] = S[k] = {S[k]}, triplet_count = {triplet_count}"
#                 )

#     return count


# def count_palindromic_triplets(S):
#     n = len(S)
#     count = 0
#     left_count = [[0] * 26 for _ in range(n)]
#     right_count = [0] * 26

#     # Left count initialization
#     for i in range(1, n):
#         for c in range(26):
#             left_count[i][c] = left_count[i - 1][c]
#         left_count[i][ord(S[i - 1]) - ord("A")] += 1

#     # Right count and calculation
#     for k in range(n - 1, 1, -1):
#         right_count[ord(S[k]) - ord("A")] += 1

#         # 中央 `j` を選んだとき、`Si == Sk` である組み合わせを確認する
#         for j in range(k - 1, 0, -1):
#             if S[j] == S[k]:
#                 triplet_count = left_count[j - 1][ord(S[j]) - ord("A")]
#                 count += triplet_count

#     return count

# def main():
#     S = input()
#     print(count_palindromic_triplets(S))


# if __name__ == "__main__":
#     main()

# from collections import defaultdict


# def main():
#     S = input().strip()
#     n = len(S)
#     count = 0
#     left_count = defaultdict(int)
#     right_count = [0] * 26

#     for k in range(n - 1, 1, -1):
#         right_count[ord(S[k]) - ord("A")] += 1
#         for j in range(k - 1, 0, -1):
#             count += left_count[ord(S[k]) - ord("A")]
#             left_count[ord(S[j]) - ord("A")] += 1

#     print(count)


# if __name__ == "__main__":
#     main()


def count_palindromic_triplets(S):
    n = len(S)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if S[i] == S[k]:
                    count += 1
    return count

def main():
    S = input()
    print(count_palindromic_triplets(S))


if __name__ == "__main__":
    main()

# S = input().strip()
# n = len(S)
# sum_count = [[0] * (n + 1) for _ in range(26)]

# for i in range(n):
#     for j in range(26):
#         sum_count[j][i + 1] = sum_count[j][i]
#     sum_count[ord(S[i]) - ord("A")][i + 1] += 1

# ans = 0
# for i in range(1, n - 1):
#     for j in range(26):
#         l = sum_count[j][i]
#         r = sum_count[j][n] - sum_count[j][i + 1]
#         ans += l * r

# print(ans)

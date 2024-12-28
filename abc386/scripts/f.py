#!/usr/bin/env python3
"""
Script Name: f.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def is_string_matched_within_k(S, T, K):
    len_S = len(S)
    len_T = len(T)

    if abs(len_S - len_T) > K:
        return False

    prefix = 0
    while prefix < len_S and prefix < len_T and S[prefix] == T[prefix]:
        prefix += 1

    suffix_S = len_S - 1
    suffix_T = len_T - 1
    while suffix_S >= prefix and suffix_T >= prefix and S[suffix_S] == T[suffix_T]:
        suffix_S -= 1
        suffix_T -= 1

    S_trimmed = S[prefix : suffix_S + 1]
    T_trimmed = T[prefix : suffix_T + 1]
    len_S_trimmed = len(S_trimmed)
    len_T_trimmed = len(T_trimmed)

    if abs(len_S_trimmed - len_T_trimmed) > K:
        return False

    dp_prev = {}
    for j in range(max(0, len_T_trimmed - K), min(len_T_trimmed, K) + 1):
        dp_prev[j] = j

    for i in range(1, len_S_trimmed + 1):
        dp_current = {}
        from_j = max(1, i - K)
        to_j = min(len_T_trimmed, i + K)
        for j in range(from_j, to_j + 1):
            if S_trimmed[i - 1] == T_trimmed[j - 1]:
                dp_current[j] = dp_prev.get(j - 1, K + 1)
            else:
                replace = dp_prev.get(j - 1, K + 1)
                insert = dp_current.get(j - 1, K + 1)
                delete = dp_prev.get(j, K + 1)
                dp_current[j] = 1 + min(replace, insert, delete)
            if dp_current[j] > K:
                dp_current[j] = K + 1
        dp_prev = dp_current

    return dp_prev.get(len_T_trimmed, K + 1) <= K


def main():
    K = int(input())
    S = input()
    T = input()

    if 1 < K <= 20 and is_string_matched_within_k(S, T, K):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

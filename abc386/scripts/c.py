#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def is_string_matched_by_replace(S, T):
    if len(S) != len(T):
        return False
    diff = 0
    for a, b in zip(S, T):
        if a != b:
            diff += 1
            if diff > 1:
                return False
    return diff == 1


def is_string_matched_by_insert(S, T):
    if len(S) + 1 != len(T):
        return False
    i = j = 0
    diff = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            j += 1
            diff += 1
            if diff > 1:
                return False
    return True


def is_string_matched_by_delete(S, T):
    if len(S) - 1 != len(T):
        return False
    i = j = 0
    diff = 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            i += 1
            j += 1
        else:
            i += 1
            diff += 1
            if diff > 1:
                return False
    return True


def is_string_matched(S, T):
    if S == T:
        return True

    return (
        is_string_matched_by_replace(S, T)
        or is_string_matched_by_insert(S, T)
        or is_string_matched_by_delete(S, T)
    )


def main():
    K = int(input())
    S = input()
    T = input()

    if K != 1:
        print("No")
        return

    if is_string_matched(S, T):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script checks if the strings match.
Author: tatsujin
Date: 2024-10-05
"""


def check_string_match_v1(S, T, min_length):
    for i in range(min_length):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        if len(S) == len(T):
            print(0)
        else:
            print(min_length + 1)


def check_string_match_v2(S, T, min_length):
    # Whole string matching.
    if S == T:
        print(0)

    # Substring matching. ex) S=abc, T=abcde
    elif S[:min_length] == T[:min_length]:
        print(min_length + 1)

    # Find mismatched characters from the beginning.
    else:
        for i in range(min_length):
            if S[i] != T[i]:
                print(i + 1)
                break


def main():
    S = input()
    T = input()
    min_length = min(len(S), len(T))

    # check_string_match_v1(S, T, min_length)
    check_string_match_v2(S, T, min_length)


if __name__ == "__main__":
    main()

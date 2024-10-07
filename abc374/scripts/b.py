#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script checks if the strings match.
Author: tatsujin
Date: 2024-10-05
"""


def check_string_match_v1(S, T, min_length):
    """
    for-else syntax
    Compares two strings and finds the first differing position using a for-else syntax.

    Args:
        S (str): The first string.
        T (str): The second string.
        min_length (int): minimum length of two strings.

    Returns:
        int: The first differing character or 0 if the strings is mached.
    """

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
    """
    if-else syntax
    Compares two strings and finds the first differing position using a if-else syntax.

    Args:
        S (str): The first string.
        T (str): The second string.
        min_length (int): minimum length of two strings.

    Returns:
        int: The first differing character or 0 if the strings is mached.
    """

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


def check_string_match_v3(S, T):
    """
    番兵 (sentinel)
    Compares two strings and finds the first differing position using a sentinel.

    Args:
        S (str): The first string.
        T (str): The second string.

    Returns:
        int: The first differing character or 0 if the strings is mached.

    Example:
        S = abc$
        T = abcde$
        result: 4
    """

    # Adds a sentinel ('$') to both strings.
    S += "$"
    T += "$"

    for i in range(len(T)):
        if S[i] != T[i]:
            print(i + 1)
            return

    print(0)


def main():
    S = input()
    T = input()

    # min_length = min(len(S), len(T))
    # check_string_match_v1(S, T, min_length)
    # check_string_match_v2(S, T, min_length)

    check_string_match_v3(S, T)


if __name__ == "__main__":
    main()

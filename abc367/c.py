#!/usr/bin/env python3
"""
Script Name: two_cards.py
Description: 
    This script finds the pair of p and q whose sum is k.
Usage:
    $ python3 two_cards.py

Author: tatsujin
Date: 2024-08-17
"""


# from itertools import product


# def output_matrix():
#     N, K = map(int, input().split())
#     r_list = list(map(int, input().split()))

#     valid_sequences = []
#     for seq in product(*(range(1, r + 1) for r in r_list)):
#         if sum(seq) % K == 0:
#             valid_sequences.append(seq)
#     valid_sequences.sort()

#     for seq in valid_sequences:
#         print(" ".join(map(str, seq)))


def generate_sequences(N, K, r_list, current_sequence=[], index=0):
    if index == N:
        if sum(current_sequence) % K == 0:
            print(" ".join(map(str, current_sequence)))
        return

    for num in range(1, r_list[index] + 1):
        generate_sequences(N, K, r_list, current_sequence + [num], index + 1)


def output_matrix():
    N, K = map(int, input().split())
    r_list = list(map(int, input().split()))

    generate_sequences(N, K, r_list)


def main():
    output_matrix()


if __name__ == "__main__":
    main()

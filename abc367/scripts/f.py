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


def find_target_pair():
    _, k = map(int, input().split())
    p_list = [int(p) for p in input().split()]
    q_list = [int(q) for q in input().split()]
    is_exist = False

    for p in p_list:
        for q in q_list:
            if p + q == k:
                is_exist = True
                break

    if is_exist:
        print("Yes")
        print(f"Found pair: p={p}, q={q}, k={k}")

    else:
        print("No")


def main():
    find_target_pair()


if __name__ == "__main__":
    main()

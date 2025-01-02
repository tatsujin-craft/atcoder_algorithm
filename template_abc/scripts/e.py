#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def get_rotate_cards(N, K, cards):
    K = K % N
    rotate_cards = cards[-K:] + cards[:-K]
    return rotate_cards


def main():
    N, K = map(int, input().split())
    cards = list(map(int, input().split()))

    rotate_cards = get_rotate_cards(N, K, cards)
    rotate_cards_str = " ".join(map(str, rotate_cards))
    print(rotate_cards_str)


if __name__ == "__main__":
    main()

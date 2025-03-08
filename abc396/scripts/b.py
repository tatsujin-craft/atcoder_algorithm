#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    q = int(input())

    card_deck = [0] * 100
    for _ in range(q):
        query = input().split()
        if query[0] == "1":
            card_deck.insert(0, int(query[1]))
        else:
            print(card_deck.pop(0))


if __name__ == "__main__":
    main()

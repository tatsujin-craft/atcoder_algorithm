#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    S = input()
    if len(S) % 2 != 0:
        print("No")
    else:
        pairs = [S[i : i + 2] for i in range(0, len(S), 2)]
        if all(pair[0] == pair[1] for pair in pairs) and all(
            S.count(c) == 2 for c in set(S)
        ):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

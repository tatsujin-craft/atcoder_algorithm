#!/usr/bin/env python3
"""
Script Name: b.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            is_match = True
            for k in range(M):
                if S[i + k][j : j + M] != T[k]:
                    is_match = False
                    break
            if is_match:
                print(i + 1, j + 1)
                exit()


if __name__ == "__main__":
    main()

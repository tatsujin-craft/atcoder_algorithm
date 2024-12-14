#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""

from itertools import combinations


def main():
    a, b, c, d, e = map(int, input().split())

    problem_letters = ["A", "B", "C", "D", "E"]
    problem_scores = [a, b, c, d, e]
    name_score_list = []

    for r in range(1, 6):
        for combo in combinations(range(5), r):
            name = "".join([problem_letters[i] for i in combo])
            score = sum([problem_scores[i] for i in combo])
            name_score_list.append((-score, name))

    name_score_list.sort()
    for item in name_score_list:
        print(item[1])


if __name__ == "__main__":
    main()

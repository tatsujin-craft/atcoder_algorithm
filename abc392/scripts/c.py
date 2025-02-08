#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def main():
    N = int(input())
    target_persons = list(map(int, input().split()))
    bib_numbers = list(map(int, input().split()))

    person_index_by_bib = [0] * N
    for i, bib_number in enumerate(bib_numbers):
        person_index_by_bib[bib_number - 1] = i

    target_person_bib_numbers = []
    for bib in range(N):
        j = person_index_by_bib[bib]
        target_person_bib_numbers.append(str(bib_numbers[target_persons[j] - 1]))

    print(" ".join(target_person_bib_numbers))


if __name__ == "__main__":
    main()

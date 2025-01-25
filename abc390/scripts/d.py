#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


from collections import defaultdict


def count_possible_xors(N, A):
    current_states = defaultdict(int)
    current_states[tuple([0] * N)] = 1

    for ai in A:
        next_states = defaultdict(int)
        for state in current_states:
            for bag in range(N):
                new_state = list(state)
                new_state[bag] += ai
                new_state_sorted = tuple(sorted(new_state))
                next_states[new_state_sorted] += 1
        current_states = next_states

    possible_xors = set()
    for state in current_states:
        xor_val = 0
        for count in state:
            xor_val ^= count
        possible_xors.add(xor_val)

    return len(possible_xors)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    result = count_possible_xors(N, A)
    print(result)


if __name__ == "__main__":
    main()

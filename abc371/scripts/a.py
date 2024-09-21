#!/usr/bin/env python3

"""
Find the 2nd son from the three brothers (A, B, C)

Exhaustive case analysis using lexicographical order of binary representation
0 0 0   < < <   A < B < C
0 0 1   < < >   A < C < B
0 1 0   < > <   NG (contradictory pattern)
0 1 1   < > >   C < A < B
1 0 0   > < <   B < A < C
1 0 1   > < >   NG (contradictory pattern)
1 1 0   > > <   B < C < A
1 1 1   > > >   C < B < A
"""


def full_pattern_analysis(S_AB, S_AC, S_BC):
    # A < B < C
    if S_AB == "<" and S_AC == "<" and S_BC == "<":
        print("B")
    # A < C < B
    elif S_AB == "<" and S_AC == "<" and S_BC == ">":
        print("C")
    # NG
    elif S_AB == "<" and S_AC == ">" and S_BC == "<":
        pass
    # C < A < B
    elif S_AB == "<" and S_AC == ">" and S_BC == ">":
        print("A")
    # B < A < C
    elif S_AB == ">" and S_AC == "<" and S_BC == "<":
        print("A")
    # NG
    elif S_AB == ">" and S_AC == "<" and S_BC == ">":
        pass
    # B < C < A
    elif S_AB == ">" and S_AC == ">" and S_BC == "<":
        print("C")
    # C < B < A
    elif S_AB == ">" and S_AC == ">" and S_BC == ">":
        print("B")


def refined_pattern_analysis(S_AB, S_AC, S_BC):
    # C < A < C, B < A < C
    if S_AB != S_AC:
        print("A")

    # A < B < C, C < B < A
    elif S_AB == S_BC:
        print("B")

    # A < C < B, B < C < A
    else:
        print("C")


def main():
    S_AB, S_AC, S_BC = input().split()

    # Full pattern
    full_pattern_analysis(S_AB, S_AC, S_BC)

    # Refined pattern
    # refined_pattern_analysis(S_AB, S_AC, S_BC)


if __name__ == "__main__":
    main()

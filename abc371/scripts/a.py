#!/usr/bin/env python3


def main():
    S_AB, S_AC, S_BC = input().split()

    if (S_AB == "<" and S_BC == "<") or (S_AB == ">" and S_AC == ">"):
        print("B")
    elif (S_AB == "<" and S_BC == ">") or (S_AB == ">" and S_AC == "<"):
        print("C")
    else:
        print("A")


def main():
    S_AB, S_AC, S_BC = input().split()

    # A < B < C
    if S_AB == "<" and S_AC == "<" and S_BC == "<":
        print("B")
    # A < C < B
    elif S_AB == "<" and S_AC == "<" and S_BC == ">":
        print("C")
    # C < A < B
    elif S_AB == "<" and S_AC == ">" and S_BC == "<":
        print("A")
    # C < B < A
    elif S_AB == "<" and S_AC == ">" and S_BC == ">":
        print("B")
    # B < A < C
    elif S_AB == ">" and S_AC == "<" and S_BC == "<":
        print("A")
    # B < C < A
    elif S_AB == ">" and S_AC == "<" and S_BC == ">":
        print("C")
    # A < B < C
    elif S_AB == ">" and S_AC == ">" and S_BC == "<":
        print("B")
    # A < C < B
    elif S_AB == ">" and S_AC == ">" and S_BC == ">":
        print("C")


if __name__ == "__main__":
    main()

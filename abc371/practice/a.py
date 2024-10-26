#!/usr/bin/env python3


def main():
    s_ab, s_ac, s_bc = input().split()
    # print(s_ab, s_ac, s_bc)

    # 000, A < B < C
    if s_ab == "<" and s_ac == "<" and s_bc == "<":
        print("B")

    # 001, A < C < B
    elif s_ab == "<" and s_ac == "<" and s_bc == ">":
        print("C")

    # 010, NG (A < B < C < A)
    elif s_ab == "<" and s_ac == ">" and s_bc == "<":
        pass

    # 011, C < A < B
    elif s_ab == "<" and s_ac == ">" and s_bc == ">":
        print("A")

    # 100, B < A < C
    elif s_ab == ">" and s_ac == "<" and s_bc == "<":
        print("A")

    # 101, NG (C < B < A < C)
    elif s_ab == ">" and s_ac == "<" and s_bc == ">":
        pass

    # 110, B < C < A
    elif s_ab == ">" and s_ac == ">" and s_bc == "<":
        print("C")

    # 111, C < B < A
    elif s_ab == ">" and s_ac == ">" and s_bc == ">":
        print("B")


if __name__ == "__main__":
    main()

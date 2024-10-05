#!/usr/bin/env python3


def main():
    S = input()
    T = input()
    min_length = min(len(S), len(T))

    for i in range(min_length):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        if len(S) == len(T):
            print(0)
        else:
            print(min_length + 1)


if __name__ == "__main__":
    main()

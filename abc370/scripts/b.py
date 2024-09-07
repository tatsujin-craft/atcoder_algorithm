#!/usr/bin/env python3


def get_final_element(N, A):
    current_element = 1
    for i in range(1, N + 1):
        if current_element >= i:
            # A_ij
            current_element = A[current_element - 1][i - 1]
        else:
            # A_ji
            current_element = A[i - 1][current_element - 1]

    return current_element


def main():
    N = int(input())
    A = []

    for _ in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    result = get_final_element(N, A)
    print(result)


if __name__ == "__main__":
    main()

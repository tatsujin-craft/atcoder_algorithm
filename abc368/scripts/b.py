#!/usr/bin/env python3


def get_repeat_count_after_operation(N, A):
    repeat_count = 0

    while True:
        # Sort descending order
        A.sort(reverse=True)

        A[0] -= 1
        if N > 1:
            A[1] -= 1

        # Increment
        repeat_count += 1

        # Count positive integers
        positive_count = sum(1 for x in A if x > 0)
        if positive_count <= 1:
            break

    return repeat_count


def main():
    N = int(input())
    A = list(map(int, input().split()))

    repeat_count = get_repeat_count_after_operation(N, A)
    print(repeat_count)


if __name__ == "__main__":
    main()

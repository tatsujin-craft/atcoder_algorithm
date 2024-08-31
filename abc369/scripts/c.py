#!/usr/bin/env python3


def get_patterns_count(N, A):
    count = 0
    for l in range(N):
        count += 1
        d = None
        for r in range(l + 1, N):
            if d is None:
                d = A[r] - A[r - 1]
            elif A[r] - A[r - 1] != d:
                break
            count += 1

    return count


# def get_patterns_count(N, A):
#     count = 0
#     l = 0

#     while l < N:
#         # 長さ1の数列は常に等差数列
#         count += 1
#         r = l + 1
#         while r < N and (A[r] - A[r - 1] == A[l + 1] - A[l] if l + 1 < N else True):
#             count += r - l
#             r += 1

#         l = r - 1

#     return count


def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(A)

    patterns_count = get_patterns_count(N, A)
    print(patterns_count)


if __name__ == "__main__":
    main()

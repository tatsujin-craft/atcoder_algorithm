#!/usr/bin/env python3

import itertools


# def find_N_and_A(M):
#     for N in range(1, 21):
#         for A in itertools.product(range(11), repeat=N):
#             total = sum(3**Ai for Ai in A)
#             if total == M:
#                 print(N)
#                 print(" ".join(map(str, A)))
#                 return


# def find_N_and_A(M):
#     powers_of_3 = [3**i for i in range(11)]

#     def backtrack(n, current_sum, A):
#         if current_sum > M:
#             return False
#         if current_sum == M:
#             print(n)
#             print(" ".join(map(str, A)))
#             return True
#         if n == 20:
#             return False

#         for i in range(11):
#             if backtrack(n + 1, current_sum + powers_of_3[i], A + [i]):
#                 return True
#         return False

#     backtrack(0, 0, [])


# def find_N_and_A(M):
#     powers_of_3 = [3**i for i in range(10, -1, -1)]
#     A = []

#     for power in powers_of_3:
#         count = 0
#         while M >= power:
#             M -= power
#             count += 1
#         if count > 0:
#             A.extend([powers_of_3.index(power)] * count)

#     print(len(A))
#     print(" ".join(map(str, A)))


# def find_N_and_A(M):
#     def backtrack(current_sum, A):
#         if current_sum == M:
#             print(len(A))
#             print(" ".join(map(str, A)))
#             return True
#         if len(A) >= 20 or current_sum > M:
#             return False

#         for i in range(11):
#             if backtrack(current_sum + 3**i, A + [i]):
#                 return True
#         return False

#     backtrack(0, [])


def find_N_and_A(M):
    powers_of_3 = [3**i for i in range(11)]
    A = []

    for i in reversed(range(11)):
        power = powers_of_3[i]
        count = 0
        while M >= power:
            M -= power
            count += 1
        if count > 0:
            A.extend([i] * count)
            # print(f"Debug: M={M}, selected Ai={i}, A={A}")

    print(len(A))
    print(" ".join(map(str, A)))


def main():
    M = int(input())
    find_N_and_A(M)


if __name__ == "__main__":
    main()

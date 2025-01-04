#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def count_snake_numbers(n):
    if n < 10:
        return 0

    digit_list = list(map(int, str(n)))
    num_digits = len(digit_list)

    precomputed_snake_counts = [0] * 20
    for k in range(1, 20):
        precomputed_snake_counts[k] = sum(d ** (k - 1) for d in range(1, 10))

    total_snake_num = sum(precomputed_snake_counts[k] for k in range(2, num_digits))

    head_digit = digit_list[0]
    for d in range(1, head_digit):
        total_snake_num += d ** (num_digits - 1)

    memoized_results = {}

    def dfs(position, is_smaller_than_n):
        if position == len(digit_list) - 1:
            return 1

        if (position, is_smaller_than_n) in memoized_results:
            return memoized_results[(position, is_smaller_than_n)]

        if not is_smaller_than_n:
            max_digit = digit_list[position + 1]
        else:
            max_digit = head_digit - 1

        count = 0
        for digit in range(max_digit + 1):
            if digit >= head_digit:
                break
            new_is_smaller = is_smaller_than_n or (digit < max_digit)
            count += dfs(position + 1, new_is_smaller)

        memoized_results[(position, is_smaller_than_n)] = count
        return count

    total_snake_num += dfs(0, False)
    return total_snake_num


def main():
    L, R = map(int, input().split())

    result = count_snake_numbers(R) - count_snake_numbers(L - 1)
    print(result)


if __name__ == "__main__":
    main()

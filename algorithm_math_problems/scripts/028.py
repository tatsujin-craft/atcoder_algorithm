#!/usr/bin/env python3
"""
Description: DP Frog jump
Author: tatsujin
Date: 2024-10-13
"""

DEBUG_LOG_ENABLED = True


def get_result_with_dp(N, H):
    dp = [float("inf")] * (N + 1)
    dp[1] = 0
    if DEBUG_LOG_ENABLED:
        print(f"Height of steps: {H}")
        print(f"Initial dp: {dp}\n")

    for i in range(2, N + 1):
        # Get minimum cost of jumping ahead one (i+1)
        dp[i] = min(dp[i], dp[i - 1] + abs(H[i - 2] - H[i - 1]))
        if DEBUG_LOG_ENABLED:
            print(f"Jump+1, step{i-1} => step{i}, dp[{i}] = {dp[i]}")

        if i > 2:
            # Get minimum cost of jumping ahead two (i+2)
            dp[i] = min(dp[i], dp[i - 2] + abs(H[i - 3] - H[i - 1]))
            if DEBUG_LOG_ENABLED:
                print(f"Jump+2, step{i-2} => step{i}, dp[{i}] = {dp[i]}")

        if DEBUG_LOG_ENABLED:
            print(f"Current position: step{i}, dp: {dp}\n")

    return dp[N]


def main():
    N = int(input())
    H = list(map(int, input().split()))

    cost = get_result_with_dp(N, H)
    if DEBUG_LOG_ENABLED:
        print(f"Minimum total cost: dp[{N}] = {cost}")
    else:
        print(cost)


if __name__ == "__main__":
    main()

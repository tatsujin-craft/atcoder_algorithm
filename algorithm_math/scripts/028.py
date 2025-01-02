#!/usr/bin/env python3
"""
Description: DP Frog jump
Author: tatsujin
Date: 2024-10-13
"""

import time


def format_large_number(n):
    """
    Args:
        n (int): large number
    Returns:
        str: Scientific notation number (a*10^b)
    """
    if n >= 1000:
        exponent = len(str(n)) - 1
        base = round(n / (10**exponent), 1)
        return f"{base}*10^{exponent}"
    return str(n)


def get_result_with_bruteforce(N, H):
    # Brute-force recursive function to calculate the minimum cost
    def find_min_cost_recursive(current_step):
        # Termination condition
        if current_step == 1:
            print(f"current step: {current_step}, cost = 0")
            return 0
        if current_step == 2:
            cost = abs(H[1] - H[0])
            print(f"current step: {current_step}, cost = {cost}")
            return cost

        # Recursive calls
        # Jump +1
        cost1 = find_min_cost_recursive(current_step - 1) + abs(
            H[current_step - 1] - H[current_step - 2]
        )
        # Jump +2
        cost2 = find_min_cost_recursive(current_step - 2) + abs(
            H[current_step - 1] - H[current_step - 3]
        )

        # After recursive calls
        min_cost = min(cost1, cost2)
        if min_cost == cost1:
            jump_type = "jump+1"
        else:
            jump_type = "jump+2"

        print(
            f"current step: {current_step}, min({cost1}, {cost2}), cost = {min_cost}, {jump_type}\n"
        )
        return min_cost

    # 1st call, and return last value
    return find_min_cost_recursive(N)


def get_result_with_dp(N, H):
    dp = [float("inf")] * (N + 1)
    dp[1] = 0
    print(f"Initial dp: {dp}\n")

    for current_step in range(2, N + 1):
        # Get minimum cost of jumping ahead +1 step
        dp[current_step] = min(
            dp[current_step], dp[current_step - 1] + abs(H[current_step - 2] - H[current_step - 1])
        )
        print(
            f"Jump+1, step{current_step-1} => step{current_step}, "
            f"dp[{current_step}] = {dp[current_step]}"
        )

        if current_step > 2:
            # Get minimum cost of jumping ahead +2 steps
            dp[current_step] = min(
                dp[current_step],
                dp[current_step - 2] + abs(H[current_step - 3] - H[current_step - 1]),
            )
            print(
                f"Jump+2, step{current_step-2} => step{current_step}, "
                f"dp[{current_step}] = {dp[current_step]}"
            )

        print(f"Current position: step{current_step}, dp: {dp}\n")

    return dp[N]


def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(f"Height of steps: {H}\n")

    # DP
    start_time = time.time()
    print("[DP]")
    cost_dp = get_result_with_dp(N, H)
    dp_time = time.time() - start_time

    # Brute-force
    start_time = time.time()
    print("[Brute force]")
    cost_brute = get_result_with_bruteforce(N, H)
    brute_time = time.time() - start_time

    # Print results
    print("\nDP")
    print(f"  Result cost: {cost_dp}")
    print(f"  Time complexity: O(N)")
    print(f"  Number of calculations: {N-1}")
    print(f"  Execution time: {dp_time:.6f} seconds")

    print("\nBrute-force")
    print(f"  Result cost: {cost_brute}")
    print(f"  Time complexity: O(2^N)")
    print(f"  Number of calculations: {format_large_number(2**N)}")
    print(f"  Execution time: {brute_time:.6f} seconds")


if __name__ == "__main__":
    main()

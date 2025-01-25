#!/usr/bin/env python3
"""
Script Name: e.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def create_dp_for_each_vitamin(items_by_vitamin, max_calorie):
    dp_list = []
    for vitamin_type in range(3):
        dp = [0] * (max_calorie + 1)
        for amount, cost in items_by_vitamin[vitamin_type]:
            for cal in range(max_calorie, cost - 1, -1):
                new_value = dp[cal - cost] + amount
                if new_value > dp[cal]:
                    dp[cal] = new_value
        dp_list.append(dp)
    return dp_list


def find_min_calories_for_vitamin(dp_for_vitamin, target_amount, max_calorie):
    low = 0
    high = max_calorie + 1
    while low < high:
        mid = (low + high) // 2
        if dp_for_vitamin[mid] >= target_amount:
            high = mid
        else:
            low = mid + 1
    if low <= max_calorie and dp_for_vitamin[low] >= target_amount:
        return low
    return float("inf")


def find_max_min_vitamin(dp_list, max_calorie):
    max_possible = min(
        dp_list[0][max_calorie], dp_list[1][max_calorie], dp_list[2][max_calorie]
    )
    low = 0
    high = max_possible + 1
    while low < high:
        mid = (low + high) // 2
        cost_0 = find_min_calories_for_vitamin(dp_list[0], mid, max_calorie)
        cost_1 = find_min_calories_for_vitamin(dp_list[1], mid, max_calorie)
        cost_2 = find_min_calories_for_vitamin(dp_list[2], mid, max_calorie)
        total_cost = cost_0 + cost_1 + cost_2
        if total_cost <= max_calorie:
            low = mid + 1
        else:
            high = mid
    return low - 1


def main():
    N, X = map(int, input().split())
    food_params = [[], [], []]
    for _ in range(N):
        v, a, c = map(int, input().split())
        food_params[v - 1].append((a, c))

    dp_list = create_dp_for_each_vitamin(food_params, X)
    result = find_max_min_vitamin(dp_list, X)
    print(result)


if __name__ == "__main__":
    main()

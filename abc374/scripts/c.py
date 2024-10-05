#!/usr/bin/env python3


# def main():
#     N = int(input().strip())
#     K = list(map(int, input().split()))
#     total_people = sum(K)

#     half_total = total_people // 2
#     dp = [False] * (half_total + 1)
#     dp[0] = True

#     for people in K:
#         for j in range(half_total, people - 1, -1):
#             dp[j] = dp[j] or dp[j - people]

#     group_a_max = 0
#     for i in range(half_total, -1, -1):
#         if dp[i]:
#             group_a_max = i
#             break

#     group_b_max = total_people - group_a_max
#     print(max(group_a_max, group_b_max))


# def main():
#     N = int(input().strip())
#     K = list(map(int, input().split()))

#     K.sort(reverse=True)
#     group_a = 0
#     group_b = 0

#     for i, people in enumerate(K):
#         if group_a <= group_b:
#             group_a += people
#             print(f"{i+1}番目の部署({people}人)をグループAに割り当てました。")
#         else:
#             group_b += people
#             print(f"{i+1}番目の部署({people}人)をグループBに割り当てました。")

#         print(f"現在のグループA: {group_a}, 現在のグループB: {group_b}\n")

#     print(max(group_a, group_b))


# def minimize_max_group_size(N, K):

#     total_sum = sum(K)
#     half_sum = total_sum // 2

#     dp = [False] * (half_sum + 1)
#     dp[0] = True

#     for k in K:
#         for j in range(half_sum, k - 1, -1):
#             dp[j] = dp[j] or dp[j - k]

#     for i in range(half_sum, -1, -1):
#         if dp[i]:
#             group_A = i
#             break

#     group_B = total_sum - group_A
#     return max(group_A, group_B)


# def optimized_greedy_minimize_max_group_size(N, K):
#     K.sort(reverse=True)  # 大きい順にソート
#     total_sum = sum(K)
#     half_sum = total_sum // 2

#     group_A = 0
#     group_B = 0
#     memo = [0] * (N + 1)

#     # グループ分けの累積和を記録し、近似解を探す
#     for i, k in enumerate(K):
#         if group_A <= group_B:
#             group_A += k
#             memo[i] = group_A
#         else:
#             group_B += k
#             memo[i] = group_B

#     # グループAの累積和とグループBの累積和を比較して、最小化する
#     group_A_final = max(memo)
#     group_B_final = total_sum - group_A_final

#     return max(group_A_final, group_B_final)


# def get_result(N, K):
#     total_sum = sum(K)
#     half_sum = total_sum // 2

#     dp = [False] * (half_sum + 1)
#     dp[0] = True

#     for k in K:
#         for j in range(half_sum, k - 1, -1):
#             dp[j] = dp[j] or dp[j - k]

#     for i in range(half_sum, -1, -1):
#         if dp[i]:
#             group_A = i
#             break

#     group_B = total_sum - group_A

#     return max(group_A, group_B)


def get_result(N, K):
    total_sum = sum(K)
    best_result = total_sum

    for i in range(1 << N):
        group_A = 0
        group_B = 0
        for j in range(N):
            if i & (1 << j):
                group_A += K[j]
            else:
                group_B += K[j]
        best_result = min(best_result, max(group_A, group_B))

    return best_result


def main():
    N = int(input())
    K = list(map(int, input().split()))
    # print(minimize_max_group_size(N, K))
    # print(optimized_greedy_minimize_max_group_size(N, K))
    result_num = get_result(N, K)
    print(result_num)


if __name__ == "__main__":
    main()

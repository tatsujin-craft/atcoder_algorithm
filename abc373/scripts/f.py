#!/usr/bin/env python3


# def knapsack_with_scores(N, W, items):
#     dp = [-float("inf")] * (W + 1)
#     dp[0] = 0

#     for i in range(N):
#         wi, vi = items[i]
#         new_dp = dp[:]
#         for weight in range(W + 1):
#             for k in range(1, (W - weight) // wi + 1):
#                 score = k * vi - k * k
#                 if weight + k * wi <= W:
#                     new_dp[weight + k * wi] = max(
#                         new_dp[weight + k * wi], dp[weight] + score
#                     )
#         dp = new_dp

#     return max(dp)


# def get_max_score(N, W, items):
#     dp = [-float("inf")] * (W + 1)
#     dp[0] = 0

#     for i in range(N):
#         wi, vi = items[i]
#         for weight in range(W, wi - 1, -1):
#             for k in range(1, weight // wi + 1):
#                 score = k * vi - k * k
#                 dp[weight] = max(dp[weight], dp[weight - k * wi] + score)

#     return max(dp)


# def get_max_score(N, W, items):
#     dp = [-float("inf")] * (W + 1)
#     dp[0] = 0

#     for i in range(N):
#         wi, vi = items[i]
#         new_dp = dp[:]
#         for weight in range(W + 1):
#             max_k = min(weight // wi, vi // 2)
#             if max_k > 0:
#                 max_score = max_k * vi - max_k * max_k
#                 new_weight = weight - max_k * wi
#                 new_dp[weight] = max(new_dp[weight], dp[new_weight] + max_score)
#         dp = new_dp

#     return max(dp)


# def get_max_score(N, W, items):
#     dp = [0] * (W + 1)

#     for i in range(N):
#         wi, vi = items[i]
#         for weight in range(W, wi - 1, -1):
#             k_max = weight // wi
#             for k in range(1, k_max + 1):
#                 score = k * vi - k * k
#                 dp[weight] = max(dp[weight], dp[weight - k * wi] + score)

#     return max(dp)


def get_max_score(N, W, items):
    dp = [[-float("inf")] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        wi, vi = items[i - 1]
        for weight in range(W + 1):
            dp[i][weight] = dp[i - 1][weight]
            for k in range(1, (weight // wi) + 1):
                score = k * vi - k * k
                dp[i][weight] = max(dp[i][weight], dp[i - 1][weight - k * wi] + score)

    return max(dp[N])


def main():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    result = get_max_score(N, W, items)
    print(result)


if __name__ == "__main__":
    main()

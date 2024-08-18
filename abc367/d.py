#!/usr/bin/env python3
"""
Script Name: two_cards.py
Description: 
    This script finds the pair of p and q whose sum is k.
Usage:
    $ python3 two_cards.py

Author: tatsujin
Date: 2024-08-17
"""


# def count_valid_pairs(rest_spot_num, factor, steps_list):
#     # 歩数の累積和を円環的に計算する
#     cumulative_sum = [0] * (2 * rest_spot_num + 1)
#     for i in range(1, 2 * rest_spot_num + 1):
#         cumulative_sum[i] = cumulative_sum[i - 1] + steps_list[(i - 1) % rest_spot_num]

#     count = 0
#     # ペアと距離をチェック
#     for i in range(rest_spot_num):
#         for j in range(i + 1, i + rest_spot_num):
#             distance = cumulative_sum[j] - cumulative_sum[i]
#             if distance % factor == 0:
#                 count += 1
#                 print(
#                     f"Valid pair: (s={i+1}, t={(j % rest_spot_num) + 1}) with distance {distance} is a multiple of {factor}"
#                 )
#             else:
#                 print(
#                     f"Invalid pair: (s={i+1}, t={(j % rest_spot_num) + 1}) with distance {distance} is not a multiple of {factor}"
#                 )

#     return count


# def main():
#     # 入力の処理
#     rest_spot_num, factor = map(int, input().split())
#     steps_list = list(map(int, input().split()))
#     print(f"rest_spot_num={rest_spot_num}, factor={factor}, steps_list={steps_list}")

#     # 関数呼び出しと結果の出力
#     result = count_valid_pairs(rest_spot_num, factor, steps_list)
#     print(f"Result: {result}")


# if __name__ == "__main__":
#     main()


# def count_valid_pairs(rest_spot_num, factor, steps_list):
#     cumulative_sum = 0
#     modulo_count = {0: 1}
#     count = 0

#     for i in range(rest_spot_num * 2):
#         cumulative_sum += steps_list[i % rest_spot_num]
#         modulo = cumulative_sum % factor

#         if modulo in modulo_count:
#             count += modulo_count[modulo]
#             modulo_count[modulo] += 1
#         else:
#             modulo_count[modulo] = 1

#     return count


# def main():
#     rest_spot_num, factor = map(int, input().split())
#     steps_list = list(map(int, input().split()))

#     result = count_valid_pairs(rest_spot_num, factor, steps_list)
#     print(f"Result: {result}")


# if __name__ == "__main__":
#     main()


# def count_valid_pairs(rest_spot_num, factor, steps_list):
#     count = 0
#     # リストを2倍にして円環状の処理を行う
#     extended_steps_list = steps_list * 2
#     modulo_count = {0: 1}
#     cumulative_sum = 0

#     for i in range(2 * rest_spot_num):
#         cumulative_sum += extended_steps_list[i]
#         modulo = cumulative_sum % factor

#         # iがrest_spot_numを超えると、(s, t)の組み合わせが重複してしまうため調整
#         if i >= rest_spot_num:
#             previous_modulo = (cumulative_sum - steps_list[i - rest_spot_num]) % factor
#             modulo_count[previous_modulo] -= 1

#         count += modulo_count.get(modulo, 0)
#         modulo_count[modulo] = modulo_count.get(modulo, 0) + 1

#     return count


# def main():
#     rest_spot_num, factor = map(int, input().split())
#     steps_list = list(map(int, input().split()))

#     result = count_valid_pairs(rest_spot_num, factor, steps_list)
#     print(f"Result: {result}")


# if __name__ == "__main__":
#     main()


def count_valid_pairs(rest_spot_num, factor, steps_list):
    cumulative_sum = [0] * (2 * rest_spot_num + 1)
    for i in range(1, 2 * rest_spot_num + 1):
        cumulative_sum[i] = cumulative_sum[i - 1] + steps_list[(i - 1) % rest_spot_num]

    count = 0
    for i in range(rest_spot_num):
        for j in range(i + 1, i + rest_spot_num):
            distance = cumulative_sum[j] - cumulative_sum[i]
            if distance % factor == 0:
                count += 1

    return count


def main():
    rest_spot_num, factor = map(int, input().split())
    steps_list = list(map(int, input().split()))

    result = count_valid_pairs(rest_spot_num, factor, steps_list)
    print(result)


if __name__ == "__main__":
    main()

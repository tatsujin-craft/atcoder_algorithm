#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def get_max_substring_length(N, S):
#     max_length = 0
#     prefix_count = 0

#     for i, char in enumerate(S):
#         if char == "1":
#             prefix_count += 1
#         elif char == "/":
#             suffix_count = 0
#             for j in range(i + 1, N):
#                 if S[j] == "2":
#                     suffix_count += 1
#                     current_length = 1 + prefix_count + suffix_count
#                     if current_length % 2 == 1:
#                         max_length = max(max_length, current_length)
#                 else:
#                     break
#             prefix_count = 0

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     # 条件を満たす部分文字列の最大長を求める
#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos
#             if current_length % 2 == 1:
#                 max_length = max(max_length, current_length)

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # デバッグ: prefix_ones 配列
#     print(f"prefix_ones: {prefix_ones}")

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     # デバッグ: suffix_twos 配列
#     print(f"suffix_twos: {suffix_twos}")

#     # 条件を満たす部分文字列の最大長を求める
#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos
#             # デバッグ: 各 `/` の位置と計算結果
#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, current_length={current_length}"
#             )
#             if current_length % 2 == 1:
#                 max_length = max(max_length, current_length)

#     # デバッグ: 最終結果
#     print(f"max_length: {max_length}")
#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos
#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, current_length={current_length}"
#             )

#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones == mid - 1 and right_twos == mid - 1:
#                     max_length = max(max_length, current_length)

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos
#             # 厳密な条件を確認
#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones == mid - 1 and right_twos == mid - 1:
#                     max_length = max(max_length, current_length)
#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, current_length={current_length}"
#             )

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 厳密な条件を確認
#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones >= mid - 1 and right_twos >= mid - 1:
#                     max_length = max(max_length, current_length)

#             # デバッグログ
#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 condition_left = left_ones >= mid - 1
#                 condition_right = right_twos >= mid - 1
#                 print(
#                     f"Checking i={i}: left_ones={left_ones}, right_twos={right_twos}, mid={mid}, "
#                     f"condition_left={condition_left}, condition_right={condition_right}"
#                 )
#                 if condition_left and condition_right:
#                     max_length = max(max_length, current_length)
#                     print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"current_length={current_length}, max_length={max_length}"
#             )

#     return max_length

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 # 修正: 左右の文字数が条件を満たすか厳密にチェック
#                 if left_ones >= mid - 1 and right_twos >= mid - 1:
#                     max_length = max(max_length, current_length)
#                     print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"current_length={current_length}, max_length={max_length}"
#             )

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 調整: 右側の 2 が不足している場合、文字列長を減らす
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos

#             # 最大値を更新
#             if current_length % 2 == 1:
#                 max_length = max(max_length, current_length)
#                 print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 調整: 右側の 2 が不足している場合
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整

#             # 最大値を更新
#             if current_length % 2 == 1:
#                 max_length = max(max_length, current_length)
#                 print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 調整: 右側の 2 が不足している場合
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整

#             # 最大値を更新 (左側も右側も十分か確認)
#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones >= mid - 1 and right_twos >= mid - 1:
#                     max_length = max(max_length, current_length)
#                     print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 調整: 右側の 2 が不足している場合
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整

#             # 最大値を更新
#             if current_length % 2 == 1:
#                 max_length = max(max_length, current_length)
#                 print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length


# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 調整: 右側の 2 が不足している場合
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整

#             # 最大値を更新 (左側も右側も十分か確認)
#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones >= mid - 1 and right_twos >= mid - 1:
#                     if current_length > max_length:  # 明示的に更新条件をチェック
#                         max_length = current_length
#                         print(f"Updating max_length: current_length={current_length}")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, max_length={max_length}"
#             )

#     return max_length

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 部分文字列を生成
#             substring = S[max(0, i - left_ones) : i + 1 + right_twos]

#             # 調整: 右側の 2 が不足している場合
#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整
#                 substring = S[max(0, i - left_ones) : i + 1 + right_twos]

#             # 最大値を更新 (左側も右側も十分か確認)
#             if current_length % 2 == 1:
#                 mid = (current_length + 1) // 2
#                 if left_ones >= mid - 1 and right_twos >= mid - 1:
#                     if current_length > max_length:  # 明示的に更新条件をチェック
#                         max_length = current_length
#                         print(f"Updating max_length: current_length={current_length}, substring='{substring}'")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, "
#                 f"substring='{substring}', max_length={max_length}"
#             )


# #     return max_length
# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 部分文字列を生成
#             left_start = i - left_ones
#             right_end = i + 1 + right_twos
#             substring = S[max(0, left_start) : min(N, right_end)]

#             # 条件修正: 左側と右側の内容を厳密に判定
#             left_valid = S[max(0, left_start) : i].count("1") == left_ones
#             right_valid = S[i + 1 : min(N, right_end)].count("2") == right_twos

#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整
#                 substring = S[max(0, left_start) : min(N, i + 1 + right_twos)]

#             # 最大値を更新 (条件を厳密に適用)
#             if current_length % 2 == 1 and left_valid and right_valid:
#                 max_length = max(max_length, current_length)
#                 print(
#                     f"Updating max_length: current_length={current_length}, substring='{substring}'"
#                 )

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, "
#                 f"substring='{substring}', max_length={max_length}"
#             )

#     return max_length

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 部分文字列を生成
#             left_start = i - left_ones
#             right_end = i + 1 + right_twos
#             substring = S[max(0, left_start) : min(N, right_end)]

#             # 条件チェック
#             left_valid = all(c == "1" for c in S[max(0, left_start):i])
#             right_valid = all(c == "2" for c in S[i + 1 : min(N, right_end)])

#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整
#                 substring = S[max(0, left_start) : min(N, i + 1 + right_twos)]

#             # 最大値を更新 (条件を厳密に適用)
#             if current_length % 2 == 1 and left_valid and right_valid:
#                 max_length = max(max_length, current_length)
#                 print(f"Updating max_length: current_length={current_length}, substring='{substring}'")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, "
#                 f"substring='{substring}', left_valid={left_valid}, right_valid={right_valid}, max_length={max_length}"
#             )

#     return max_length

# def main():
#     N = int(input())
#     S = input()

#     max_length = get_max_substring_length(N, S)
#     print(max_length)


# if __name__ == "__main__":
#     main()

# def get_max_substring_length(N, S):
#     prefix_ones = [0] * N
#     suffix_twos = [0] * N

#     # 前計算: 各位置までの '1' の累積個数
#     for i in range(N):
#         if S[i] == "1":
#             prefix_ones[i] = prefix_ones[i - 1] + 1 if i > 0 else 1
#         else:
#             prefix_ones[i] = prefix_ones[i - 1] if i > 0 else 0

#     # 後計算: 各位置から始まる '2' の連続個数
#     for i in range(N - 1, -1, -1):
#         if S[i] == "2":
#             suffix_twos[i] = suffix_twos[i + 1] + 1 if i < N - 1 else 1
#         else:
#             suffix_twos[i] = 0

#     max_length = 0
#     for i in range(N):
#         if S[i] == "/":
#             left_ones = prefix_ones[i - 1] if i > 0 else 0
#             right_twos = suffix_twos[i + 1] if i < N - 1 else 0
#             current_length = 1 + left_ones + right_twos

#             # 必要な右側の 2 の数を計算
#             mid = (current_length + 1) // 2
#             needed_twos = mid - 1

#             # 部分文字列を生成
#             left_start = i - left_ones
#             right_end = i + 1 + right_twos
#             substring = S[max(0, left_start) : min(N, right_end)]

#             # 条件チェック (左側と右側の値を厳密に確認)
#             left_valid = S[max(0, left_start):i] == "1" * left_ones
#             right_valid = S[i + 1 : min(N, right_end)] == "2" * right_twos

#             if right_twos < needed_twos:
#                 current_length = 1 + left_ones + right_twos
#                 if current_length % 2 == 0:
#                     current_length -= 1  # 奇数に調整
#                 substring = S[max(0, left_start) : min(N, i + 1 + right_twos)]

#             # 最大値を更新 (条件を厳密に適用)
#             if current_length % 2 == 1 and left_valid and right_valid:
#                 max_length = max(max_length, current_length)
#                 print(f"Updating max_length: current_length={current_length}, substring='{substring}'")

#             print(
#                 f"i={i}, left_ones={left_ones}, right_twos={right_twos}, "
#                 f"needed_twos={needed_twos}, current_length={current_length}, "
#                 f"substring='{substring}', left_valid={left_valid}, right_valid={right_valid}, max_length={max_length}"
#             )

#     return max_length


def get_max_substring_length(N, S):
    max_length = 0

    for i in range(N):
        if S[i] != "/":
            continue

        d = 0
        while True:
            j = i - (d + 1)
            k = i + (d + 1)

            if not (0 <= j < N and 0 <= k < N):
                break
            if S[j] != "1" or S[k] != "2":
                break

            d += 1

        max_length = max(max_length, 1 + d * 2)

    return max_length


def main():
    N = int(input())
    S = input()

    max_length = get_max_substring_length(N, S)
    print(max_length)


if __name__ == "__main__":
    main()

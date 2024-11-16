#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


# def get_result_string(S, Q, queries):
#     def find_char(k):
#         k -= 1
#         while k >= len(S):
#             length = len(S)
#             while length * 2 <= k + 1:
#                 length *= 2
#             if k == length:
#                 k = length - 1
#             else:
#                 k = k - length - 1
#             if k < 0:
#                 k += length
#             if k < len(S):
#                 return S[k] if k % 2 == 0 else S[k].swapcase()
#         return S[k]

#     result = [find_char(k) for k in queries]
#     result_string = " ".join(result)
#     return result_string


def get_result_string(S, Q, queries):
    n = len(S)
    lengths = [n]

    # 各操作段階での文字列の長さを計算
    while lengths[-1] < 10**18:
        lengths.append(lengths[-1] * 2)

    def find_char(k):
        k -= 1
        flip = 0
        # 段階をさかのぼって元の位置を探す
        while k >= n:
            length = n
            step = len(lengths) - 1
            # 長さのリストから段階を特定
            while step > 0 and lengths[step - 1] > k:
                step -= 1
            # 反転部分にいるかを確認
            if k >= lengths[step - 1]:
                k -= lengths[step - 1] + 1
                flip ^= 1
        # 最終的な文字を返す
        return S[k].swapcase() if flip else S[k]

    result = [find_char(k) for k in queries]
    return " ".join(result)


def main():
    S = input()
    Q = int(input())
    queries = list(map(int, input().split()))

    result_string = get_result_string(S, Q, queries)
    print(result_string)


if __name__ == "__main__":
    main()

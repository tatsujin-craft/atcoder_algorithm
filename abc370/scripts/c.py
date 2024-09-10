#!/usr/bin/env python3


# def get_x_list(S, T):
#     X = []
#     s_list = list(S)
#     t_list = list(T)
#     i = 0

#     while s_list != t_list:
#         if s_list[i] != t_list[i]:
#             s_list[i] = t_list[i]
#             X.append("".join(s_list))
#         i += 1

#     return X

# 惜しい
# def get_x_list(S, T):
#     X = []
#     s_list = list(S)
#     t_list = list(T)

#     # 文字列を辞書順最小に変更しつつ T に一致させる
#     for i in range(len(S)):
#         # まずSのi番目の文字がTと異なる場合
#         if s_list[i] != t_list[i]:
#             # まずSのi番目の文字を辞書順で最小に近づける
#             for j in range(i + 1, len(S)):
#                 if s_list[j] != t_list[j]:
#                     s_list[j] = min(s_list[j], t_list[j])
#                     X.append("".join(s_list))

#             # 次にSのi番目の文字をTの文字に変更
#             s_list[i] = t_list[i]
#             X.append("".join(s_list))

#     return X


# def get_x_list(S, T):
#     X = []
#     s_list = list(S)
#     t_list = list(T)

#     for i in range(len(S)):
#         if s_list[i] != t_list[i]:
#             for j in range(i + 1, len(S)):
#                 if s_list[j] != t_list[j]:
#                     s_list[j] = min(s_list[j], t_list[j])
#                     new_state = "".join(s_list)
#                     if new_state not in X:
#                         X.append(new_state)

#             s_list[i] = t_list[i]
#             new_state = "".join(s_list)
#             if new_state not in X:
#                 X.append(new_state)

#     return X


def get_x_list(S, T):
    ans = []  # 操作の結果を格納するリスト
    n = len(S)  # 文字列の長さ

    # SとTが一致するまで操作を続ける
    while S != T:
        nxt = "z" * n  # 次の状態を辞書順最大の文字列で初期化
        for i in range(n):
            if S[i] != T[i]:
                tmp = list(S)  # 一時的なコピーを作成
                tmp[i] = T[i]  # i番目の文字を変更
                tmp = "".join(tmp)  # リストを文字列に戻す
                nxt = min(nxt, tmp)  # 辞書順最小の状態を更新
        ans.append(nxt)  # 最小の状態を結果に追加
        S = nxt  # Sを次の状態に更新

    return ans


def main():
    S = input().strip()
    T = input().strip()

    X = get_x_list(S, T)
    print(len(X))
    for item in X:
        print(item)


if __name__ == "__main__":
    main()

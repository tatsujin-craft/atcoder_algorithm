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


def get_x_list(S, T):
    X = []
    s_list = list(S)
    t_list = list(T)

    for i in range(len(S)):
        if s_list[i] != t_list[i]:
            for j in range(i + 1, len(S)):
                if s_list[j] != t_list[j]:
                    s_list[j] = min(s_list[j], t_list[j])
                    new_state = "".join(s_list)
                    if new_state not in X:
                        X.append(new_state)

            s_list[i] = t_list[i]
            new_state = "".join(s_list)
            if new_state not in X:
                X.append(new_state)

    return X


def main():
    S = input().strip()
    T = input().strip()

    X = get_x_list(S, T)
    print(len(X))
    for item in X:
        print(item)


if __name__ == "__main__":
    main()

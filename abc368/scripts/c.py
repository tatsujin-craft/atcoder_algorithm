#!/usr/bin/env python3


# def get_turns_to_defeat_enemies(N, hitpoints):
#     max_time = 0  # 全ての敵が倒されるのに必要な最長時間を格納する変数

#     for hitpoint in hitpoints:
#         # 各敵の体力に対して必要な時間を計算
#         # Tが3の倍数の場合、体力を3で割る
#         # Tが3の倍数でない場合、まず体力から1を引いて、その後で3で割る

#         # Tが3の倍数のとき
#         times_if_t_mult_of_3 = (hitpoint + 2) // 3

#         # 最も大きなTを求める
#         max_time = max(max_time, times_if_t_mult_of_3 * 3)

#     return max_time


# def get_turns_to_defeat_enemies(hitpoints):
#     max_turns = 0
#     for hp in hitpoints:
#         # 各敵が倒れるまでのターン数を計算する
#         turns = 0

#         # 3回ごとのダメージを適用
#         turns = hp // 5 * 3
#         remaining_hp = hp % 5

#         # 残りの体力を処理
#         if remaining_hp > 0:
#             if remaining_hp == 1 or remaining_hp == 2:
#                 turns += 1  # 1点または2点のダメージで足りる
#             else:
#                 turns += 2  # 3点ダメージで確実に0以下に

#         # 最大ターン数を更新
#         max_turns = max(max_turns, turns)

#     return max_turns


# def get_turns_to_defeat_enemies(hitpoints):
#     max_turns = 0
#     for hp in hitpoints:
#         # 各敵が倒れるまでのターン数を計算
#         damage_3_turns = (hp + 2) // 3  # 3の倍数ターンで全ダメージを計算
#         actual_turns = damage_3_turns

#         # 3の倍数のターン数から実際のダメージを計算
#         total_damage_3_turns = damage_3_turns // 3 * 3 + (damage_3_turns % 3)
#         remaining_hp = hp - total_damage_3_turns

#         # 残りの体力に対して1点ダメージターンが必要かどうか
#         if remaining_hp > 0:
#             actual_turns += (remaining_hp + 2) // 3

#         # 最大ターン数を更新
#         max_turns = max(max_turns, actual_turns)

#     return max_turns


def get_result_by_brute_force(hitpoints):
    T = 0
    for hp in hitpoints:
        turns = 0
        while hp > 0:
            if (T + 1) % 3 == 0:
                hp -= 3
            else:
                hp -= 1
            turns += 1
            T += 1
    return T


def get_result_by_efficient_algorithm(hitpoints):
    T = 0
    for hp in hitpoints:
        num = hp // 5
        T += num * 3
        hp -= num * 5
        while hp > 0:
            T += 1
            if T % 3 == 0:
                hp -= 3
            else:
                hp -= 1
    return T


def main():
    _ = int(input())
    hitpoints = list(map(int, input().split()))
    print(hitpoints)

    T = get_result_by_efficient_algorithm(hitpoints)
    print(T)

    # T = get_result_by_brute_force(hitpoints)
    # print(T)


if __name__ == "__main__":
    main()

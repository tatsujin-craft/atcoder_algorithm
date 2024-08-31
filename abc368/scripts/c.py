#!/usr/bin/env python3


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

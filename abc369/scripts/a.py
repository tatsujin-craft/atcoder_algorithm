#!/usr/bin/env python3


# def get_x_pattern_num(A, B):
#     x_pattern_num = set()

#     # x = B + (B - A) / 2
#     if (B - A) % 2 == 0:
#         x_pattern_num.add(B + (B - A) // 2)
#     # x = A + (A - B) / 2
#     if (A - B) % 2 == 0:
#         x_pattern_num.add(A + (A - B) // 2)

#     # x = 2A - B
#     x_pattern_num.add(2 * A - B)
#     # x = 2B - A
#     x_pattern_num.add(2 * B - A)

#     return len(x_pattern_num)


def get_x_pattern_num(A, B):
    x_min = 2 * B - A
    x_max = 2 * A - B
    x_mid = (A + B) // 2

    x_pattern_num = set()

    if A != B:
        x_pattern_num.add(x_min)
        x_pattern_num.add(x_max)

    if (A + B) % 2 == 0:
        x_pattern_num.add(x_mid)

    return len(x_pattern_num)


def main():
    A, B = map(int, input().split())
    # print(A, B)
    x_pattern_num = get_x_pattern_num(A, B)
    print(x_pattern_num)


if __name__ == "__main__":
    main()

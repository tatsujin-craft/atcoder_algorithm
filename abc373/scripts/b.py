#!/usr/bin/env python3


def calculate_alphabet_distance(S):
    total_distance = 0
    previous_position = ord(S[0]) - ord("A")

    for i in range(1, len(S)):
        current_position = ord(S[i]) - ord("A")
        total_distance += abs(current_position - previous_position)
        previous_position = current_position

    return total_distance


def calculate_total_distance(S):
    keyboard = list(S)
    current_position = keyboard.index("A")
    total_distance = 0

    for target_char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        target_position = keyboard.index(target_char)
        total_distance += abs(target_position - current_position)
        current_position = target_position

    return total_distance


def main():
    S = input().strip()
    total_distance = calculate_total_distance(S)
    print(total_distance)


if __name__ == "__main__":
    main()

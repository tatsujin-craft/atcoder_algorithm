#!/usr/bin/env python3


def calculate_tiredness_score(piano_actions):
    left_hand_position = None
    right_hand_position = None
    score = 0

    for action in piano_actions:
        key_number = int(action[0])
        hand = action[1]

        if hand == "L":
            if left_hand_position is not None:
                score += abs(key_number - left_hand_position)
            left_hand_position = key_number
        elif hand == "R":
            if right_hand_position is not None:
                score += abs(key_number - right_hand_position)
            right_hand_position = key_number

    return score


def main():
    N = int(input().strip())
    piano_actions = [input().strip().split() for _ in range(N)]
    # print(piano_actions)

    tiredness_score = calculate_tiredness_score(piano_actions)
    print(tiredness_score)


if __name__ == "__main__":
    main()

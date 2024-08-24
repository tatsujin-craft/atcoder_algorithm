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


def check_shout():
    shout_time, sleep_time, wake_time = map(int, input().split())
    is_shout = True

    if sleep_time < wake_time:
        is_shout = not (sleep_time <= shout_time < wake_time)
    else:
        is_shout = not (sleep_time <= shout_time or shout_time < wake_time)

    if is_shout:
        print("Yes")
    else:
        print("No")


def main():
    check_shout()


if __name__ == "__main__":
    main()

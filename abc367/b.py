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

from decimal import Decimal


def main():
    x = Decimal(input())
    print(x.normalize())


if __name__ == "__main__":
    main()

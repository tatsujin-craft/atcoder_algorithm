#!/usr/bin/env python3
"""
Script Name: c.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def process_queries(queries):
    cumulative_sum = [0]
    front_index = 0
    removed_sum = 0
    outputs = []

    for query in queries:
        if query[0] == "1":
            length = int(query[1])
            cumulative_sum.append(cumulative_sum[-1] + length)
        elif query[0] == "2":
            removed_sum += cumulative_sum[front_index + 1] - cumulative_sum[front_index]
            front_index += 1
        else:
            k = int(query[1])
            snake_index = front_index + k - 1
            head_coordinate = cumulative_sum[snake_index] - removed_sum
            outputs.append(str(head_coordinate))

    print("\n".join(outputs))


def main():
    Q = int(input())
    queries = [input().split() for _ in range(Q)]

    process_queries(queries)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


# def count_abc(s):
#     return s.count("ABC")


# def process_queries(s, queries):
#     results = []
#     s = list(s)

#     for xi, ci in queries:
#         s[xi - 1] = ci
#         results.append(count_abc("".join(s)))

#     return results


# def count_abc_at_pos(s, pos):
#     if pos < 0 or pos + 2 >= len(s):
#         return 0
#     return 1 if s[pos : pos + 3] == "ABC" else 0


def count_abc_at_pos(s, pos):
    if pos < 0 or pos + 2 >= len(s):
        return 0
    if s[pos] == "A" and s[pos + 1] == "B" and s[pos + 2] == "C":
        return 1
    return 0


def process_queries(s, queries):
    results = []
    s = list(s)
    current_count = 0

    for i in range(len(s) - 2):
        current_count += count_abc_at_pos(s, i)
    # print(f"Initial 'ABC' count: {current_count}")

    for xi, ci in queries:
        xi -= 1
        # print(f"\nProcessing query: change s[{xi}] to '{ci}'")

        for i in range(xi - 2, xi + 1):
            if 0 <= i <= len(s) - 3:
                abc_before = count_abc_at_pos(s, i)
                current_count -= abc_before
                # if abc_before > 0:
                #     print(f"Removing 'ABC' at pos {i} before update")
        s[xi] = ci

        for i in range(xi - 2, xi + 1):
            if 0 <= i <= len(s) - 3:
                abc_after = count_abc_at_pos(s, i)
                current_count += abc_after
                # if abc_after > 0:
                #     print(f"Adding 'ABC' at pos {i} after update")

        # print(f"After query, S: {''.join(s)}")
        # print(f"'ABC' count after query: {current_count}")

        results.append(current_count)

    return results


def main():
    _, Q = map(int, input().split())
    S = input()
    queries = [input().split() for _ in range(Q)]
    queries = [(int(x), c) for x, c in queries]

    results = process_queries(S, queries)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

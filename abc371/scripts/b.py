#!/usr/bin/env python3


def check_first_son(children_info):
    is_first_son_borned = {}
    results = []

    for family_num, gender_char in children_info:
        if gender_char == "M":
            # First son (Does the key exist in dict ?)
            if family_num not in is_first_son_borned:
                is_first_son_borned[family_num] = True
                results.append("Yes")
            # Other son
            else:
                results.append("No")
        # Daughter
        else:
            results.append("No")

    return results


def main():
    _, M = map(int, input().split())
    # Get information of M children
    children = [input().split() for _ in range(M)]
    # Convert data format from 2D list to tuple list
    children_info = [(int(child[0]), child[1]) for child in children]

    # Get result
    results = check_first_son(children_info)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()

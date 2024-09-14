#!/usr/bin/env python3


def check_first_son(N, M, children):
    first_son_status = {}
    results = []

    for house_number, gender in children:
        if gender == "M":
            if house_number not in first_son_status:
                first_son_status[house_number] = True
                results.append("Yes")
            else:
                results.append("No")
        else:
            results.append("No")

    return results


def main():
    N, M = map(int, input().split())
    children = [input().split() for _ in range(M)]
    children = [(int(child[0]), child[1]) for child in children]
    results = check_first_son(N, M, children)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3


def check_first_son(children_info):
    is_first_son_dict = {}

    for family_id, gender in children_info:
        if gender == "M":
            # Does the key exist in the dictionary ?
            if family_id not in is_first_son_dict:
                print("Yes")
                is_first_son_dict[family_id] = True
                # print(is_first_son_dict)
            else:
                print("No")
        else:
            print("No")


def main():
    N, M = map(int, input().split())
    children = [input().split() for _ in range(M)]
    # print(children)
    children_info = [(int(child[0]), child[1]) for child in children]
    # print(children_info)

    check_first_son(children_info)


if __name__ == "__main__":
    main()

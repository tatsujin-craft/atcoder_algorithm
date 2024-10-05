#!/usr/bin/env python3


# def main():
#     S = input().strip()

#     if "san" in S:
#         print("Yes")
#     else:
#         print("No")


def main():
    S = input().strip()

    if S.endswith("san"):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

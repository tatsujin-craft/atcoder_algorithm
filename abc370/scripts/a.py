#!/usr/bin/env python3


def main():
    L, R = map(int, input().split())

    if L == True and R == False:
        print("Yes")
    elif L == False and R == True:
        print("No")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()

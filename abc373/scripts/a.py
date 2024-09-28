#!/usr/bin/env python3


def main():
    count = 0
    for i in range(12):
        s = input()
        if len(s) == i + 1:
            count += 1
        # print(s, len(s), i)

    print(count)


if __name__ == "__main__":
    main()

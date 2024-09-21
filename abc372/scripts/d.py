#!/usr/bin/env python3


# def count_buildings(N, heights):
#     result = []
#     for i in range(N):
#         count = 0
#         for j in range(i + 1, N):
#             if all(heights[k] <= heights[j] for k in range(i + 1, j)):
#                 count += 1
#         result.append(count)
#     return result


# def count_buildings(N, heights):
#     result = []
#     stack = []

#     # ビルを右から左に見ていく
#     for i in range(N - 1, -1, -1):
#         count = 0
#         while stack and heights[i] >= heights[stack[-1]]:
#             stack.pop()
#         count = len(stack)
#         stack.append(i)
#         result.append(count)

#     # 結果を逆順にして返す
#     result.reverse()
#     return result


# def count_buildings(N, heights):
#     result = [0] * N
#     stack = []

#     for i in range(N - 1, -1, -1):
#         while stack and heights[i] > heights[stack[-1]]:
#             stack.pop()
#         result[i] = len(stack)
#         stack.append(i)

#     return result


# def count_buildings(N, heights):
#     result = []
#     max_right = 0
#     for i in range(N - 1, -1, -1):
#         if heights[i] > max_right:
#             max_right = heights[i]
#         count = 0
#         for j in range(i + 1, N):
#             if heights[j] >= heights[i]:
#                 count += 1
#             if heights[j] > heights[i]:
#                 break
#         result.append(count)
#         print(f"Building {i+1} (height {heights[i]}): Count {count}")
#     result.reverse()
#     return result


# def count_buildings(N, heights):
#     result = []
#     for i in range(N):
#         count = 0
#         max_height = heights[i]
#         for j in range(i + 1, N):
#             if heights[j] >= heights[i]:
#                 count += 1
#             if heights[j] > max_height:
#                 max_height = heights[j]
#             if heights[j] > heights[i]:
#                 break
#         result.append(count)
#         print(f"Building {i+1} (height {heights[i]}): Count {count}")
#     return result


# stack
# def count_buildings(N, heights):
#     result = [0] * N
#     stack = []

#     for i in range(N - 1, -1, -1):
#         while stack and heights[i] > heights[stack[-1]]:
#             stack.pop()
#         result[i] = len(stack)
#         stack.append(i)
#         # print(f"Building {i+1} (height {heights[i]})")

#     return result


# submit, TLE
def count_buildings(N, heights):
    result = []
    for i in range(N):
        count = 0
        max_height = 0
        for j in range(i + 1, N):
            if heights[j] > max_height:
                max_height = heights[j]
            if max_height <= heights[j]:
                count += 1
        # print(f"Building {i+1} (height {heights[i]}): Count {count}")
        result.append(count)
    return result


def main():
    N = int(input())
    heights = list(map(int, input().split()))

    output = count_buildings(N, heights)
    print(" ".join(map(str, output)))


if __name__ == "__main__":
    main()

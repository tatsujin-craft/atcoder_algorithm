#!/usr/bin/env python3


def get_result(N, K):
    total_people = sum(K)
    best_result = total_people

    print(f"\nTotal people: {total_people}")
    print(f"Team number: {N}, Total attempts: {2**N}")

    # Bitwise exhaustive search (bit全探索) 2^N
    for i in range(1 << N):
        group_A = 0
        group_B = 0
        print(f"\nPattern{i+1}: {bin(i)[2:].zfill(N)}")

        # Add the number of people in the bit=1 group
        for j in range(N):
            # Bit AND operation (A: bit=1, B: bit=0)
            if i & (1 << j):
                group_A += K[j]
            else:
                group_B += K[j]

        # Get max people from A and B
        current_result = max(group_A, group_B)
        print(f"A: {group_A}, B: {group_B}, max people: {current_result}")

        # Update best result
        best_result = min(best_result, current_result)

    print(f"\nBest result (minimum max people): {best_result}")
    return best_result


def main():
    N = int(input())
    K = list(map(int, input().split()))

    result_num = get_result(N, K)
    print(result_num)


if __name__ == "__main__":
    main()

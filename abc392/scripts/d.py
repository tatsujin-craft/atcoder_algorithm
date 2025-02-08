#!/usr/bin/env python3
"""
Script Name: d.py
Description: This script is a template.
Author: tatsujin
Date: xxxx-yy-zz
"""


def find_max_probability(N, face_count_maps, side_counts):
    max_probability = 0.0
    for i in range(N):
        for j in range(i + 1, N):
            probability = 0.0
            if len(face_count_maps[i]) < len(face_count_maps[j]):
                for face_value, count_i in face_count_maps[i].items():
                    if face_value in face_count_maps[j]:
                        count_j = face_count_maps[j][face_value]
                        probability += (count_i / side_counts[i]) * (
                            count_j / side_counts[j]
                        )
            else:
                for face_value, count_j in face_count_maps[j].items():
                    if face_value in face_count_maps[i]:
                        count_i = face_count_maps[i][face_value]
                        probability += (count_i / side_counts[i]) * (
                            count_j / side_counts[j]
                        )
            if probability > max_probability:
                max_probability = probability
    return max_probability


def main():
    N = int(input())
    face_count_maps = []
    side_counts = []
    for _ in range(N):
        data = list(map(int, input().split()))
        k = data[0]
        faces = data[1:]
        count_map = {}
        for face_value in faces:
            count_map[face_value] = count_map.get(face_value, 0) + 1
        face_count_maps.append(count_map)
        side_counts.append(k)

    max_probability = find_max_probability(N, face_count_maps, side_counts)
    print("{:.10f}".format(max_probability))


if __name__ == "__main__":
    main()

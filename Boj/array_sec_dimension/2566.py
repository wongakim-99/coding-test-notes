# 백준 2566 - 행렬 최댓값

import sys

def solution() -> None:
    # 1. 행렬 A 입력받기
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    max_val = -1
    row, col = 0, 0

    for i in range(9):
        for j in range(9):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                row, col = i + 1, j + 1

    print(max_val)
    print(row, col)


if __name__ == "__main__":
    solution()
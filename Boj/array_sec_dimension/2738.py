# 백준 2738 - 행렬 덧셈

import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().split())

    # 1. 첫 번째 행렬 A 입력 받기
    matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 2. 두 번째 행렬 B 입력 받기
    matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 3. 행렬 출력
    for i in range(n):
        for j in range(m):
            print(matrix_a[i][j] + matrix_b[i][j], end = ' ')
        print()


if __name__ == "__main__":
    solution()
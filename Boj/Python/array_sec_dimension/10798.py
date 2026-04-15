# 백준 10798 - 세로읽기

import sys


def solution() -> None:
    # 1. 행렬 입력받기
    matrix_a = [list(map(str, sys.stdin.readline().strip())) for _ in range(5)]

    # 2. 테스트 행렬 출력
    # 세로로 읽기 (최대 15열)
    for i in range(15):     # i : 열 인덱스 (0 ~ 14)
        for j in range(5):  # j : 행 인덱스 (0 ~ 4)
            # 중요 : 현재 행(matrix_a[j])의 길이가 현재 열 인덱스(i)보다 클 때만 출력
            if i < len(matrix_a[j]):
                print(matrix_a[j][i], end = '')


if __name__ == "__main__":
    solution()
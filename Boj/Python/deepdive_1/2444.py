# 별 찍기

import sys

def solution() -> None:
    num: int = int(sys.stdin.readline())

    for i in range(1, num + 1):
        print(" " * (num - i) + "*" * (2 * i - 1))

    for j in range(num - 1, 0, -1):
        print(" " * (num - j) + "*" * (2 * j - 1))

if __name__ == "__main__":
    solution()
'''
문제 생략
'''

import sys

from typing import Tuple

# 내 풀이
def solution() -> Tuple[int, int]:
    h, m = map(int, sys.stdin.readline().split())

    if m >= 45:
        return h, m - 45
    else:
        if h == 0:
            h = 23
            m = 60 - (45 - m)
            return h, m
        else:
            h -= 1
            m = 60 - (45 - m)
            return h, m


if __name__ == "__main__":
    print(*solution())
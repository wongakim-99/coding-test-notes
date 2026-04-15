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


# 2. 조금 더 간결하게 코드 작성 version
def solution2() -> Tuple[int, int]:
    h, m = map(int, sys.stdin.readline().split())

    if m >= 45:
        return h, m - 45
    else:
        '''
        Python 에서 (음수 % 양수)는 항상 양수가 나온다.
        Python 의 모듈러 연산은 항상 양수 결과를 보장한다.
        '''
        h = (h - 1) % 24
        m = m + 15   # 60 - (45 - m) == m + 15  -> 대수적으로 정리
        return h, m


if __name__ == "__main__":
    print(*solution2())
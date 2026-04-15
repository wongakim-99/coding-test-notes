# 팰린드롬인지 확인하기

import sys

from typing import List

# 1. 내 풀이
# 틀렸는데, 알고보니 엣지 케이스인 0이나 1을 고려하지 않았음.
def solution() -> None:
    str_p: List[str] = list(sys.stdin.readline().strip())

    str_len: int = len(str_p)
    result: int = 1
    
    for i in range(str_len // 2):
        if str_p[i] != str_p[str_len - i - 1]:
            result = 0
            break
            
    print(result)


# 2. 파이썬의 슬라이싱 기법 활용
def solution2() -> None:
    pal: List[str] = list(sys.stdin.readline().strip())

    print(1 if pal == pal[::-1] else 0)

    
if __name__ == "__main__":
    solution2()
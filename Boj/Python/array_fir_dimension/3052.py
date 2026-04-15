'''
문제
두 자연수 A와 B가 있을 때, A%B는 A를 B로 나눈 나머지 이다. 예를 들어, 7, 14, 27, 38을 3으로 나눈 나머지는 1, 2, 0, 2이다.

수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

입력
첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.

출력
첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.
'''

import sys

from typing import Set  # 파이썬 3.9 미만 버전에선 필요, 3.9 이상은 생략 가능
# 현재 나는 파이썬 3.12 버젼을 사용하는 중이지만, 타입힌트를 사용하기 위해 명시적으로 넣긴 함

# 1. 내 풀이 - 중복을 제거해주는 집합 자료구조 활용
def solution1():
    remainder = set()

    for _ in range(10):
        num = int(sys.stdin.readline())
        remainder.add(num % 42)

    result = len(remainder)
    return result


# 2. 파이썬의 Generator Expression 활용
def solution2():
    # 10번 입력을 받아 42로 나눈 나머지를 바로 set으로 만듬
    return len({int(sys.stdin.readline()) % 42 for _ in range(10)})


# 3. 파이썬 코드에서 타입 힌트(Type Hint)를 적용한 코드
def solution3() -> int:
    # remainder 변수가 int를 담는 set 임을 명시
    remainder: set[int] = set()

    for _ in range(10):
        line = sys.stdin.readline()

        if not line:  # 빈 문자열을 False로 취급
            # 예외처리 느낌
            continue

        # num 변수가 int 임을 명시
        num: int = int(line)
        remainder.add(num % 42)

    # result 변수가 int임을 명시
    result: int = len(remainder)
    return result


if __name__ == "__main__":
    print(solution3())

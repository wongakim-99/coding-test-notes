'''
문제

문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
'''

import sys

# 1. 내 풀이
def solution() -> None:

    # 반복할 횟수 변수는 int 형으로 명시
    num: int = int(sys.stdin.readline())

    result = []
    for _ in range(num):
        r_num, s = sys.stdin.readline().split()
        r: int = int(r_num)

        for i in range(len(s)):
            print(s[i] * r, end='')
        print()

    print(*result)


# 2. 리스트 컴프리헨션 방식 (join 문 반복)
from typing import List

def solution2() -> None:
    # 1. 첫 번째 줄에서 테스트 케이스 개수 받기
    line: str = sys.stdin.readline().strip()

    if not line:
        return

    t_count: int = int(line)

    # 2. t_count 만큼 반복하여 한 줄씩 읽기
    for _ in range(t_count):
        # 한 줄을 읽어서 바로 split()
        # 입력 예 : "3 ABC" -> ["3", "ABC"]
        data: List[str] = sys.stdin.readline().split()

        if not data:
            continue

        r: int = int(data[0])
        s: str = data[1]

        # 3. 로직부 (동일)
        result: str = "".join([char * r for char in s])

        # 4. 출력 (엔터 치자마자 바로 결과)
        print(result)


if __name__ == "__main__":
    solution2()
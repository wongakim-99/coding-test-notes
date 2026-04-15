'''
문제

상근이의 할머니는 아래 그림과 같이 오래된 다이얼 전화기를 사용한다.

전화를 걸고 싶은 번호가 있다면, 숫자를 하나를 누른 다음에 금속 핀이 있는 곳 까지 시계방향으로 돌려야 한다. 숫자를 하나 누르면 다이얼이 처음 위치로 돌아가고, 다음 숫자를 누르려면 다이얼을 처음 위치에서 다시 돌려야 한다.
숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.


입력
첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.


출력
첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.
'''


import sys

from typing import List


# 1. 내 풀이
def solution() -> int:
    data: List[str] = list(sys.stdin.readline().strip())

    result: int = 0

    # 다이얼에 저장된 번호를 통해 직접 노가다로 해결..? 아니면 더 좋은 방법이 있을까?
    for i in range(len(data)):
        if data[i] in ['A', 'B', 'C']:
            result += 3
        elif data[i] in ['D', 'E', 'F']:
            result += 4
        elif data[i] in ['G', 'H', 'I']:
            result += 5
        elif data[i] in ['J', 'K', 'L']:
            result += 6
        elif data[i] in ['M', 'N', 'O']:
            result += 7
        elif data[i] in ['P', 'Q', 'R', 'S']:
            result += 8
        elif data[i] in ['T', 'U', 'V']:
            result += 9
        elif data[i] in ['W', 'X', 'Y', 'Z']:
            result += 10

    return result


# 2. 리스트 활용
# 알파벳 뭉치를 리스트에 담고, 그 리스트의 인덱스 활용하는 방법
def solution2() -> int:
    # 각 인덱스가 다이얼 숫자와 매칭되도록 구성
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    word: List[str] = list(sys.stdin.readline().strip())

    result = 0

    for char in word:
        for i in range(len(dial)):
            if char in dial[i]:
                result += (i + 3)

    return result


# 3. 딕셔너리 활용
# 알파벳 뭉치를 딕셔너리에 담고, 미리 모든 알파벳에 대해 시간을 매핑하면 if 문 없이 바로 값을 꺼낼 수 있다.
def solution3() -> int:
    # 딕셔너리 컴프리헨션으로 매핑 테이블 생성 (미리 선언해도 됨)
    # 실제로는 'A' : 3, 'B' : 3, 'C' : 3 ... 식으로 저장됨
    time_map = {}
    dial = {
        3 : 'ABC',
        4 : 'DEF',
        5 : 'GHI',
        6 : 'JKL',
        7 : 'MNO',
        8 : 'PQRS',
        9 : 'TUV',
        10 : 'WXYZ'
    }

    for time, chars in dial.items():
        for char in chars:
            time_map[char] = time

    word = sys.stdin.readline().strip()

    return sum(time_map[char] for char in word)


if __name__ == "__main__":
    print(solution())
'''
문제

영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까?
이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

입력
첫 줄에 영어 대소문자와 공백으로 이루어진 문자열이 주어진다.
이 문자열의 길이는 1,000,000을 넘지 않는다. 단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다.
또한 문자열은 공백으로 시작하거나 끝날 수 있다

출력
첫째 줄에 단어의 개수를 출력한다.
'''

import sys

# 타입힌트 적용을 위한 import
from typing import List

# 1. 내 풀이
def solution1() -> int:
    # 1. 문자열 입력받기
    data: List[str] = sys.stdin.readline().split()
    result: int = int(len(data))

    return result


# 2. 다른 추가된 타입힌트 외 제약사항 : 예외처리
def solution2() -> int:
    try:
        # 1. 입력시도
        data: List[str] = sys.stdin.readline().split()

        # 2. 데이터가 아예 없는 경우에 대한 예외 처리 (Optional)
        if not data:
            return 0

        return len(data)

    except EOFError:
        # 입력이 갑자기 끊기거나 파일 끝에 도달했을 때
        return 0
    except Exception as e:
        # 그 외 예상치 못한 모든 에러 처리
        print(f"Unexpected error : {e}")
        return 0


if __name__ == "__main__":
    word_len = solution2()
    print(word_len)
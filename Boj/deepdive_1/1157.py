
import sys

from typing import List

def solution() -> None:
    word: str = sys.stdin.readline().strip().upper()

    ascii_list = []

    for i in range(65, 91):
        ascii_list.append(word.count(chr(i)))

    max_count = max(ascii_list)
    if ascii_list.count(max_count) > 1:
        print("?")
    else:
        max_index = ascii_list.index(max_count)
        print(chr(max_index + 65))


def solution2() -> None:
    # 1. 일단 입력값을 대문자로 모두 바꿔줘야 함
    word: str = sys.stdin.readline().strip().upper()

    # 2. 조금 더 효율적으로 생각해서 알파벳 26개를 모두 뒤질 필요가 있을까?
    # 들어온 글자만 생각해보자 -> 중복을 제거해주는 set() 함수 활용
    unique_chars = set(word)
    print(unique_chars)

    # 3. list-comprehension 방식을 사용하여 각 글자가 몇 번 나오는지 세서 리스트에 담는다.
    counts = [word.count(c) for c in unique_chars]
    print(counts)

    # 4. 최대값이 몇 개인지 확인
    max_chars = max(counts)

    if counts.count(max_chars) > 1:
        print("?")
    else:
        # 5. 최대값의 위치(index)를 찾아 해당 알파벳 출력
        max_index = counts.index(max_chars)
        print(list(unique_chars)[max_index])


if __name__ == "__main__":
    solution2()
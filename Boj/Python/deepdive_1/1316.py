# 백준 1316 그룹 단어 체커

'''
# 1. 글자가 바뀔 때만 확인
- aaaa 처럼 같은 글자가 연속될 때는 아무 문제가 없음
- 우리가 주의 깊게 봐야 할 시점은 현재 글자가 앞의 글자와 달라지는 순간이다.

# 2. 이미 나왔던 글자 목록을 만들어라
- 단어를 한 글자씩 확인하면서, 새로운 글자가 등장하면 리스트(또는 집합)에 저장해 둔다.
- 만약 현재 글자가 앞 글자와 다른데, 이 글자가 이미 리스트에 있다면?
  그건 이전에 나왔다가 떨어져서 다시 나타났다는 뜻이므로 그룹 단어가 아니다.
'''

import sys


def solution() -> int:
    num: int = int(sys.stdin.readline())

    group_word_count: int = 0

    for _ in range(num):
        word: str = sys.stdin.readline().strip()

        # 이미 등장한 글자를 저장할 리스트 (매 단어마다 초기화)
        another_list: list = []
        is_group_word = True  # 일단 그룹 단어라고 생각하기

        for char in range(len(word)):
            # 1. 처음 등장하는 글자인가?
            if word[char] not in another_list:
                another_list.append(word[char])

            # 2. 이미 등장했던 글자인데, 바로 전 글자와 다른가? (떨어져서 다시 나옴)
            # char > 0 조건을 넣어 첫 글자일 때의 에러를 방지한다.
            elif word[char] != word[char - 1]:
                is_group_word = False
                break

        if is_group_word:
            group_word_count += 1

    return group_word_count


if __name__ == "__main__":
    print(solution())
'''
문제
도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.

도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.

공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)

도현이는 입력으로 주어진 순서대로 공을 교환한다.
'''

import sys

# 1. 내 풀이
def solution1():
    n, m = map(int, sys.stdin.readline().split())

    array = []
    for i in range(1, n + 1):
        array.append(i)

    for idx in range(m):
        i, j = map(int, sys.stdin.readline().split())
        array[i - 1], array[j - 1] = array[j - 1], array[i - 1]

    return array


# 2. 조금 더 파이썬 스럽게 내장 함수인 리스트 컴프리헨션 적용
def solution2():
    n, m = map(int, sys.stdin.readline().split())

    # 배열에 정해진 값을 집어넣는 조금 더 간결한 방식(리스트 컴프리헨션)
    array = [i for i in range(1, n + 1)]

    # 더 간결한 방식인 아래처럼 할 수도 있음
    # array = list(range(1, n + 1))

    for idx2 in range(m):
        i, j = map(int, sys.stdin.readline().split())
        array[i - 1], array[j - 1] = array[j - 1], array[i - 1]

    return array


# 3. (참고) Dictionary를 이용한 최적화 코드
def solution3():
    # N은 10억, M은 100이라고 가정
    n, m = map(int, sys.stdin.readline().split())

    # 전체 리스트 만들지 않고, 바뀐 정보만 담을 딕셔너리 생성
    changed_buckets = {}

    for _ in range(m):
        i, j = map(int, sys.stdin.readline().split())

        # 1. 현재 i 번과 j번 바구니에 든 공의 번호를 가져옴
        # 딕셔너리에 없으면 (기본값) 바구니 번호 자체가 공의 번호임
        ball_i = changed_buckets.get(i, i)
        print(ball_i, "\n")
        ball_j = changed_buckets.get(j, j)
        print(ball_j, "\n")

        # 2. 두 공을 교환해서 저장
        changed_buckets[i] = ball_j
        changed_buckets[j] = ball_i

    # 출력 (만약 전체를 다 출력해야 한다면 N이 클 때 불가능하지만,
    # 특정 범위나 바뀐 것만 출력한다면 아래와 같이 확인 가능
    # for k in range(1, n + 1):
    #     print(changed_buckets.get(k, k), end = ' ')

    final_state = [changed_buckets.get(k, k) for k in range(1, n + 1)]
    return final_state


if __name__ == "__main__":
    # print("")
    result = solution3()
    print(*result)

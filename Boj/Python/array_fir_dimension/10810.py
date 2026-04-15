'''
도현이는 바구니를 총 N개를 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.

또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.

가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.

도현이는 앞으로 M번 공을 넣으려고 한다. 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는
공을 넣는다.

만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.
'''

import sys

# 1. 내 풀이 (가장 직관적인 브루트 포스 방식)
def solution(n, m):
    bucket = [0] * n

    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().split())

        for b in range(i - 1, j):
            bucket[b] = k

    return bucket


# 2. 리스트 슬라이싱 (파이썬의 축복 : 가장 파이썬다운 방식)
def solution2(n, m):
    bucket = [0] * n

    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().split())

        # 슬라이싱을 이용한 일괄 대입
        # bucket[i - 1] 부터 bucket[j - 1]까지를 [k, k, k, k,...]로 한 번에 갈아끼운다.
        bucket[i - 1 : j] = [k] * (j - i + 1)

    return bucket


# 3. 역발상 : 거꾸로 채우기
def solution3(n, m):
    bucket = [0] * n
    filled_count = 0

    # 쿼리를 리스트에 다 담아두고 뒤에서부터 확인
    queries = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    for q_idx in range(m - 1, -1, -1):
        i, j, k = queries[q_idx]

        for b in range(i - 1, j):
            if bucket[b] == 0:  # 아직 한 번도 안 채워진 바구니라면 (가장 마지막 작업)
                bucket[b] = k
                filled_count += 1

        if filled_count == n:   # 모든 바구니가 다 찼으면 조기 종료
            break

    return bucket


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    result = solution3(N, M)

    # 리스트 요소를 공백으로 구분해서 출력
    print(*result)
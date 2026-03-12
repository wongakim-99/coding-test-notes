# 백준 2750번
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 공통 GLOBAL 변수

import time
import random
import sys

lists = []

# 백준 문제풀때 이 부분 주석해제
# n = int(input())

# for i in range(n):
#     k = int(input())
#     lists.append(k)

# 재귀 깊이 제한 해제 (혹시 나중에 퀵 정렬 등을 위해 필요할 수 있음
sys.setrecursionlimit(10**6)


# 성능 체크 함수 - 시간복잡도 O(n^2) 알고리즘이 얼마나 똥망 알고리즘인지 체크용
def check_performance():
    # 테스트 할 데이터 크기 리스트 (N이 2배가 될 때 시간이 어떻게 변하는지 확인)
    data_size = [500, 1000, 2000]

    for n in data_size:
        print(f"\n ---데이터 크기(N) : {n}---")

        # 1. 최악의 경우 (내림차순 정렬 데이터)
        # O(n^2) 알고리즘이 가장 고통받는 상황
        worst_data = list(range(n, 0, -1))

        # 2. 랜덤 데이터 (평균적인 경우)
        random_data = [random.randint(1, n) for _ in range(n)]

        # 3. 측정할 정렬 함수들
        sort_functions = [
            ("Bubble Sort", bubble_sort),
            ("Select Sort", select_sort)
        ]

        for name, func in sort_functions:
            # 원본 데이터 보존을 위해 복사본 사용
            data_copy = worst_data[:]

            start = time.time()
            func(data_copy)
            end = time.time()

            print(f"[{name}] 최악의 경우 소요 시간 : {end - start:.4f}초")



# 아래는 각종 정렬알고리즘 관련 함수들

# ---------------------------------- #
'''
# 1. 버블 정렬
- 인접한 두 수를 비교하며 정렬해나가는 방법으로 O(n^2)의 느린 성능을 가지고 있다
- 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해나가는 방법 또는 뒤에서부터 반복하여 앞의 작은 값부터 정렬을 완성해나가는 방법이 있다
'''

def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    # for x in range(n):
    #     print(array_fir_dimension[x])

# ---------------------------------- #
'''
# 2. 선택정렬
- 핵심 : 한 바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬
- 앞에서부터 정렬해나가는 특성을 가지고 있고 버블 정렬과 마찬가지로 최악의 성능을 가진 알고리즘
'''

def select_sort(array):
    n = len(array)

    # 1. 배열의 처음부터 끝까지 훓으며 기준점(i)를 정한다
    for i in range(n):
        # 2. 현재 i 번째 자리를 '가장 작은 값이 있는 곳' 이라고 가정
        min_index = i

        # 3. i 뒤에 있는 나머지 숫자들 중 진짜 최솟값이 있는지 찾는다
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # 4. 찾은 진짜 최솟값(min_index)과 현재 자리(i)를 맞바꾼다 (Swap)
        array[i], array[min_index] = array[min_index], array[i]

    # for x in array_fir_dimension:
    #     print(x)

if __name__ == "__main__":
    # bubble_sort(lists)
    # select_sort(lists)
    check_performance()








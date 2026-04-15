# '''
# 문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
#
# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다
# '''
#
import sys


# 파이썬 내장 함수 count 함수 사용
def solution1():
    # 1. 첫째줄 입력받기
    N = int(sys.stdin.readline())

    # 2. 공백으로 입력받기
    # numbers 는 list 형태
    numbers = list(map(int, sys.stdin.readline().split()))

    # 원하는 숫자 갯수 찾기
    v = int(sys.stdin.readline())

    return numbers.count(v)


# 직접 Loop 구현
def solution2():
    # 1. 첫째줄 입력받기
    N = int(sys.stdin.readline())

    # 2. 공백으로 입력받기
    # numbers 는 list 형태
    numbers = list(map(int, sys.stdin.readline().split()))

    # 원하는 숫자 갯수 찾기
    v = int(sys.stdin.readline())

    count = 0
    for x in numbers:
        if x == v:
            count += 1

    return count

if __name__ == "__main__":
    print(solution2())


# import sys
# import time
# import random
#
#
# # 1. 내장 함수 count 사용
# def solution1(numbers, v):
#     start = time.perf_counter()
#     res = numbers.count(v)
#     end = time.perf_counter()
#     return res, end - start
#
#
# # 2. 직접 Loop 구현
# def solution2(numbers, v):
#     start = time.perf_counter()
#     count = 0
#     for x in numbers:
#         if x == v:
#             count += 1
#     end = time.perf_counter()
#     return count, end - start
#
#
# if __name__ == "__main__":
#     # 테스트용 대량 데이터 생성 (1,000,000개)
#     print("🚀 1,000,000개의 데이터를 생성 중입니다...")
#     test_data = [random.randint(-100, 100) for _ in range(1000000)]
#     target_v = 7  # 찾을 숫자
#
#     # sol1 테스트
#     res1, time1 = solution1(test_data, target_v)
#     print(f"\n[1. 내장 함수 count()]")
#     print(f"결과: {res1}개 발견")
#     print(f"소요 시간: {time1:.6f} 초")
#
#     # sol2 테스트
#     res2, time2 = solution2(test_data, target_v)
#     print(f"\n[2. 직접 구현한 Loop]")
#     print(f"결과: {res2}개 발견")
#     print(f"소요 시간: {time2:.6f} 초")
#
#     # 결과 분석
#     diff = time2 / time1
#     print(f"\n🔥 내장 함수가 직접 짠 루프보다 약 {diff:.1f}배 빠릅니다!")
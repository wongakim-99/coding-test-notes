import sys

# 0. 배열 출력처리 함수
def output_arr(n, m, array):
    for i in range(n):
        for j in range(m):
            print(array[i][j], end = " ")
        print()


# 1. 배열 입력처리 함수
def input_arr():
    # 1. 첫째 줄에 배열의 크기 N,M 수행해야 하는 연산의 수 R 제공
    n, m, r = map(int, sys.stdin.readline().split())

    # 2. 배열 입력받기
    # 한 줄을 읽어와 공백으로 나누고 숫자로 바꾼 뒤, 이를 N번 반복하여 리스트로 변환
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 3. 마지막 줄에 수행해야 하는 배열 연산
    operations = list(map(int, sys.stdin.readline().split()))

    return arr, operations


# 2. 1번 연산 함수
def solution_1(array):
    # 파이썬 슬라이싱
    array.reverse()
    return array


# 3. 2번 연산 함수
def solution_2(array):
    for row in array:
        row.reverse()
    return array


# 4. 3번 연산 함수
def solution_3(array):
    print("")



if __name__ == "__main__":
    current_arr, ops = input_arr()

    # 1. 여러 연산을 순서대로 하나씩 꺼내기
    for cmd in ops:
        # 2. cmd 번호에 따라 어떤 함수를 실행할지 분기 처리 (if/elif)
        if cmd == 1:
            current_arr = solution_1(current_arr)
        elif cmd == 2:
            current_arr = solution_2(current_arr)

    # 3. 모든 연산이 완전히 끝난 후의 행과 열 크기를 구함
    final_rows = len(current_arr)
    final_cols = len(current_arr[0])

    # 4. 최종 결과만 한 번 출력
    output_arr(final_rows, final_cols, current_arr)
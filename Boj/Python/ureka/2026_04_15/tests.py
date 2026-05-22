oimport sys

# 1. 배열 입력 및 연산 정보 수집 함수
def input_arr():
    # N, M, R 입력
    n, m, r = map(int, sys.stdin.readline().split())

    # 2D 배열 생성
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 수행해야 할 연산들 (보통 여러 개가 들어오므로 리스트로 받음)
    # 만약 한 개만 들어온다면 int(sys.stdin.readline())
    operations = list(map(int, sys.stdin.readline().split()))

    # 생성된 배열과 연산 정보를 밖으로 내보냄
    return arr, operations

# 2. 1번 연산 함수 (상하 반전)
def solution_1(array):
    # 파이썬 슬라이싱 [::-1]을 사용하면 행 순서를 아주 쉽게 뒤집을 수 있습니다.
    # 혹은 array.reverse()를 사용해도 됩니다.
    return array[::-1]


if __name__ == "__main__":
    current_arr, ops = input_arr()

    # 1. 여러 연산을 순서대로 하나씩 꺼내기
    for cmd in ops:
        # 2. cmd 번호에 따라 어떤 함수를 실행할지 분기 처리 (if/elif)
        if cmd == 1:
            current_arr = solution_1(current_arr)
        elif cmd == 2:
            # current_arr = solution_2(current_arr)
            pass


        # 1. 행(Row)의 개수
rows = len(current_arr)

# 2. 열(Column)의 개수
# 0번째 행이 가진 원소의 개수를 세면 됩니다.
cols = len(current_arr[0])

print(rows, cols)

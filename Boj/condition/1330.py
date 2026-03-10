# 손 풀기 연습문제
# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램 작성

A, B = map(int, input().split())  # 한 줄에 여러개를 입력받기 위해서는 map 함수를 사용한다

def condition_check(num_a, num_b):
    if num_a > num_b:
        return ">"
    elif num_a == num_b:
        return "=="
    else:
        return "<"

if __name__ == "__main__":
    print(condition_check(A, B))

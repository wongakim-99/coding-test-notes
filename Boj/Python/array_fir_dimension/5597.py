'''
문제
X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.

교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.

입력
입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

출력
출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
'''

import sys

# 1. 내 풀이
def solution1():
    # student_num 배열에는 1부터 30까지 저장되어 있음
    student_num = [i for i in range(1, 31)]
    not_criminal_student = []

    # 과제 안낸 범인 2명 찾기
    for _ in range(28):
        criminal = int(sys.stdin.readline())
        not_criminal_student.append(criminal)

    for i in student_num:
        if i not in not_criminal_student:
            print(i)


# 2. 집합(Set) 자료구조 활용
def solution2():
    # 1. 전체 학생 집합 (1 ~ 30)
    all_students = set(range(1, 31))

    # 2. 제출한 학생 집합
    submitted_students = set()
    for _ in range(28):
        submitted_students.add(int(sys.stdin.readline()))

    # 3. 차집합으로 과제 안 낸 범인 찾기 (전체 - 제출자)
    criminal_students = sorted(list(all_students - submitted_students))

    for student in criminal_students:
        print(student)


# 3. 불리언 리스트 (Check Array) 활용
def solution3():
    # 31칸짜리 출석부
    attendance = [False] * 31

    for _ in range(28):
        num = int(sys.stdin.readline())
        attendance[num] = True

    for i in range(1, 31):
        if not attendance[i]:
            print(i)


if __name__ == "__main__":
    # solution1()
    solution3()
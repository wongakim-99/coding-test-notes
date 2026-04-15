# 백준 25206 - 너의 평점은

import sys

def solution() -> float:
    # 과목별 등급
    grade_map = {
        "A+": 4.5, "A0": 4.0,
        "B+": 3.5, "B0": 3.0,
        "C+": 2.5, "C0": 2.0,
        "D+": 1.5, "D0": 1.0,
        "F": 0.0
    }

    total_score = 0
    total_credit = 0
    for i in range(20):
        line = sys.stdin.readline().split()

        if not line:
            break

        name, credit, grade = line   # 리스트 언패킹
        credit = float(credit)       # 학점은 실수로 변환

        # P 등급은 계산에서 제외
        if grade == "P":
            continue

        score = grade_map[grade]
        total_score += (score * credit)
        total_credit += credit

    result: float = total_score / total_credit
    return round(result, 6)


if __name__ == "__main__":
    print(solution())
# 시험 성적
'''
90 ~ 100 : A
80 ~ 89 : B
70 ~ 79 : C
60 ~ 69 : D
else: F
'''

test_result = int(input())

def test_result_check(score):
    if (score >= 90) and (score <= 100):
        print("A")
    elif (score >= 80) and (score <= 89):
        print("B")
    elif (score >= 70) and (score <= 79):
        print("C")
    elif (score >= 60) and (score <= 69):
        print("D")
    else:
        print("F")

if __name__ == "__main__":
    test_result_check(test_result)
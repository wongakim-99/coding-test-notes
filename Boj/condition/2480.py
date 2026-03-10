# 주사위 세개
'''
1. 같은 눈이 3개가 나오면 10,000원 + (같은 눈) x 1,000 원의 상금을 받게 된다
2. 같은 눈이 2개만 나오는 경우에는 1,000원 + (같은 눈) x 100원의 상금을 받게 된다
3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈) x 100원의 상금을 받게 된다
'''

'''
문제 후기 : 비교적 가벼운 문제긴 하고 직관적으로 바로 풀 수 있는 문제긴 하나 
이런 간단한 문제에도 여러 방식이 있단걸 깨달음
그리고 각각의 방식에 대하여 함수로 모듈화를 진행하여 다양한 방식에 대한 접근을 해보는 것이 중요하다고 생각함

tmi : 각 방식에 대해서 시간 복잡도는 데이터가 3개밖에 없으므로 시간 복잡도는 O(1) 이지만 데이터가 많아지면 많아질 수록
정렬을 활용하는 방식이 더 효율적이 될 수도 있음

주사위가 10,000개가 되었다고 했을때 처음의 내 방식인 if - else 방식에는 한계가 있음
이럴때 정렬방식이나 집합연산 방식을 사용하면 좋을듯

정렬 : O(NlogN)
집합 : O(N)
'''


A, B, C = map(int, input().split())

# 정렬 풀이 방식을 위한 변수
L = sorted([A, B, C])

# 1. 내 풀이 : 정석 루트대로
def condition_check_root(num_a, num_b, num_c):

    # 1. 세 눈이 모두 같은 경우
    if (num_a == num_b) and (num_b == num_c):
        # 3단 논법에 의거하여 a == b, b == c, 고로 a == c : 왜냐하면 둘다 참이여야 통과되는 and 연산자를 사용
        return 10000 + (num_a * 1000)

    # 2. 두 눈만 같은 경우
    elif (num_a == num_b) or (num_b == num_c) or (num_a == num_c):
        if num_a == num_b:
            return 1000 + (num_a * 100)
        elif num_b == num_c:
            return 1000 + (num_b * 100)
        else:
            return 1000 + (num_c * 100)

    # 3. 세 눈이 모두 다른 경우
    else:
        max_num = max(num_a, num_b, num_c)
        return max_num * 100


# 2. 정렬을 활용한 경우
def condition_check_sort(nums):
    # 1. 세 개의 눈이 모두 같은 경우 (정렬했을 때 첫번째와 마지막 눈이 모두 같음)
    if nums[0] == nums[2]:
        return 10000 + (nums[0] * 1000)

    # 2. 두 개의 눈만 같은 경우
    elif (nums[0] == nums[1]) or (nums[1] == nums[2]):  # 정렬을 했으므로 nums[1]의 숫자는 무조건 중복된 것 중 하나임
        return 1000 + (nums[1] * 100)

    # 3. 세 개의 눈이 모두 다른 경우 (정렬된 상태이므로 마지막 숫자가 가장 큰 숫자)
    else:
        return 100 * nums[2]


# 3. 파이썬 set 집합을 활용한 경우 -> 중복을 제거후 중복되지 않은 눈의 개수 카운트
def condition_check_set(a, b, c):
    dice = [a, b, c]
    unique_elements = set(dice)  # 중복 제거
    count = len(unique_elements)   # 중복되지 않은 눈의 개수

    # 1. 모든 눈이 같은 경우 (집합의 원소가 1)
    if count == 1:
        return 10000 + a * 1000

    # 2. 두 개의 눈만 같은 경우 (집합의 원소가 2)
    elif count == 2:
        # 어떤 숫자가 중복되었는지 찾는 간단한 트릭
        # (세 눈의 총합) - (집합 원소들의 총합) = 중복된 숫자
        # 예 : [3, 3, 6] -> 총합 12, 집합 {3, 6}의 총합 9, -> 12 - 9 = 3 (중복된 숫자)
        same_num = sum(dice) - sum(unique_elements)
        return 1000 + same_num * 100

    # 3. 모두 다른 눈의 겨우 (집합의 원소가 3개)
    else:
        return max(dice) * 100


if __name__ == "__main__":
    # 1. 테스트 케이스 정의 (입력값 리스트, 기대 결과값)
    # [(주사위 눈 리트스), 기대 상금]
    test_cases = [
        ([3, 3, 6], 1300),
        ([2, 2, 2], 12000),
        ([6, 2, 5], 600),
        ([1, 1, 1], 11000),  # 추가 케이스
        ([4, 4, 1], 1400),  # 추가 케이스
    ]

    print(f"{'입력값':<15} | {'정렬 풀이':<10} | {'집합 풀이':<10} | {'결과'}")
    print("-" * 55)

    for dice, expected in test_cases:
        # 각 함수 실행 (정렬 풀이는 리스트가 정렬되어 있어야 하므로 sorted 적용)

        # 1. 정렬 함수 테스트 케이스 실행
        res_sort = condition_check_sort(sorted(dice))

        # 2. 집합 조건 테스트 케이스 실행
        res_set = condition_check_set(dice[0], dice[1], dice[2])

        # 두 풀이 방식이 모두 정답과 일치하는지 확인
        is_passed = (res_sort == expected) and (res_set == expected)
        status = "✅ PASS" if is_passed else "❌ FAIL"

        print(f"{str(dice):<15} | {res_sort:<10} | {res_set:<10} | {status}")

    # print(condition_check_sort(L))
    # print(condition_check_root(A, B, C))
    print(condition_check_set(A, B, C))
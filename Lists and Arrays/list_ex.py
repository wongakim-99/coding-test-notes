# 리스트 생성
# 대괄호 [] 를 사용하여 빈 리스트를 생성하거나, 값을 포함해 생성할 수 있다.

empty_list = []
numbers = [1, 2, 3, 4]
mixed_list = [1, "Hello", 3.5, True]

# 리스트 주요 메서드
# 추가하기
numbers.append(5)  # append : 리스트의 맨 뒤에 요소를 추가 
print(numbers, "\n")

numbers.insert(1, 1.5)  # inser(index, value) : 지정한 인덱스에 요소 삽입
print(numbers, "\n")

numbers.extend([6, 7])  # extend(iterable) : 리스트를 다른 리스트나 iterable로 확장
print(numbers, "\n")


# 제거하기
numbers.remove(3)  # remove(value) : 리스트에서 첫 번째로 일치하는 요소 제거, 만약 없는 값 적으면 ValueError 발생 
print(numbers, "\n")

numbers.pop(1)  # pop(index) : 특정 인덱스의 요소를 제거하고 반환(인덱스 생략 시 마지막 요소 제거)
print(numbers, "\n")

numbers.pop()   # 인덱스 생략시 마지막 요소 제거 후 반환하는지 확인
print(numbers, "\n")

numbers.clear()  # clear() : 모든 요소 제거
print(numbers, "\n")


# 탐색 및 정렬
numbers = [1, 2, 3, 4, 5, 3, 3, 3]

print(numbers.index(3), "\n")   # index(value) : 특정 값의 인덱스 반환
print(numbers.count(3), "\n")   # count(value) : 특정 값의 개수 반환

numbers.sort()  # sort() : 리스트 오름차순 정렬(내림차순 : sort(reverse = True))
print(numbers, "\n")

numbers.sort(reverse=True)  # 내림차순 정렬
print(numbers, "\n")

numbers.reverse()  # 역순 정렬
print(numbers, "\n")
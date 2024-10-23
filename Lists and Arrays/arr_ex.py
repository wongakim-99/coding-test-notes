# 1. 배열 초기화 및 기본 연산
import array as arr

# 정수 배열 생성
my_array = arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 배열의 길이 확인
print("배열의 길이 : ", len(my_array), "\n")

# 배열의 모든 요소 출력
print("배열의 모든 요소 출력 : ")
for element in my_array:
    print(element)
print("\n")



# 2. 배열 슬라이싱
# 배열 슬라이싱
print("배열 슬라이싱 1 : ", my_array[1:4])  # 인덱스 1부터 4까지 출력 (끝 인덱스는 포함X)
print("배열 슬라이싱 2 : ", my_array[2:])  # 인덱스 2부터 끝까지 출력 
print("배열 슬라이싱 3 : ", my_array[:6])  # 인덱스 0부터 6까지 출력 (끝 인덱스는 포함되지 않음)
print("배열 슬라이싱 4 : ", my_array[::-1])  # 인덱스 거꾸로 출력 
print("배열 슬라이싱 5 : ", my_array[9:1:-2])  # 인덱스를 거꾸로 출력하되, 끝 인덱스가 2인 요소까지 출력
print("배열 슬라이싱 6 : ", my_array[1:6:2], "\n")  # 인덱스를 건너뛰어 추출하기



# 3. 배열에 여러 요소 삽입하기
# 배열의 특정 위치에 요소 삽입(insert 사용)
print("삽입 전 배열 : ", my_array) 
my_array.insert(2, 11)  # 인덱스 2에 11 삽입
print("삽입 후 배열 : ", my_array, "\n")  # 한 칸씩 밀려난다.

# 배열의 끝에 여러 요소 추가(extend 사용)
my_array.extend([12,13,14])
print("여러 요소 추가 후 배열 : ", my_array, "\n")



# 4. 배열의 요소 제거
# 배열에서 특정 인덱스의 요소 제거(pop사용)
my_array.pop(2)  # 인덱스 2의 요소 제거(11)
print("인덱스 2 제거 후 배열 : ", my_array, "\n")

# 배열에서 특정 값 제거(remove 사용)
my_array.remove(7)
my_array.remove(8)
print("7을 제거한 후에 배열 : ", my_array, "\n")



# 5. 배열의 요소 역순 정렬
my_array.reverse()
print("역순 배열 : ", my_array, "\n")



# 6. 배열의 복사
copied_arr = my_array[:]
print("복사된 배열 : ", copied_arr, "\n")



# 7. 배열에서 최대, 최소 값 찾기
# 배열에서 최소값, 최대값 찾기
print("최소값 : ", min(my_array))
print("최대값 : ", max(my_array))



# 8. 배열의 메모리 효율성
print("\n배열의 버퍼 크기 : ", my_array.buffer_info())  # 시작주소, 배열 크기
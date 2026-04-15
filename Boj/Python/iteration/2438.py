'''
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
'''

import sys

def print_start(number):
    for i in range(1, number + 1):
        print("*" * i)

if __name__ == "__main__":
    num = int(sys.stdin.readline())

    print_start(num)

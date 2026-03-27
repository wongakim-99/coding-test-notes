# 백준 2941 크로아티아 알파벳

import sys

def solution() -> int:
    croatia_alpha: list[str] = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    input_alpha: str = sys.stdin.readline().strip()

    for char in croatia_alpha:
        if char in input_alpha:
            input_alpha = input_alpha.replace(char, "*")

    return len(input_alpha)

if __name__ == "__main__":
    print(solution())
# 자료구조 스택에 대한 기본 예시

class Stack:
    """
    파이썬 리스트를 활용한 스택 클래스 구현
    """

    def is_empty(self):
        """
        스택이 비어있는지 확인합니다.
        비어있으면 True, 아니면 False를 반환합니다.
        """
        return not self.items

    def __init__(self):
        """스택을 초기화 해주는 함수. 내부적으로는 리스트 활용"""
        self.items = []
        print("📌스택이 생성되었음")

    def push(self, item):
        """
        스택의 가장 위에 데이터를 추가합니다. (Push 함수)
        """
        self.items.append(item)
        print(f"➕Push 함수 실행됨 : {item} (현재 스택 : {self.items})")

    def pop(self):
        """
        스택의 가장 맨 위의 데이터를 제거하고 그 값을 반환합니다. (Pop)
        스택이 비어있으면 에러 메시지를 출력하고 None 을 반환합니다.
        """
        if self.is_empty():
            print("Stack Underflow error : 스택이 비어있습니다.")
            return None

        popped_item = self.items.pop()
        print(f" Pop : {popped_item} (현재 스택 : {self.items})")
        return popped_item

    def peek(self):
        """
        스택의 가장 위 데이터를 확인하는 함수
        스택이 비어있으면 에러메시지를 출력하고 None 을 반환합니다.
        """
        if self.is_empty():
            print("Stack is empty : 스택이 비어있습니다.")
            return None

        peeked_item = self.items[-1]
        print(f" Peek : {peeked_item} (현재 스택 : {self.items})")
        return peeked_item

    def size(self):
        """
        스택에 들어있는 데이터의 개수를 반환합니다.
        비어있으면 True, 아니면 Fasle 를 반환합니다.
        """
        current_size = len(self.items)
        print(f" Current stack size : {current_size} (현재 스택 : {self.items})")
        return current_size


def main():
    """
    사용자 입력을 받아 스택을 제어하는 메인함수
    """
    stack = Stack()
    print("사용자와 상호작용 가능한 스택 프로그램 시작")
    print("사용 가능한 명령어 : push [value], pop, peek, size, is_empty, view, exit")

    while True:
        # 사용자로부터 명령어 입력받기
        user_input = input("\n> ").strip().lower().split()

        if not user_input:
            continue

        command = user_input[0]

        if command == "push":
            if len(user_input) > 1:
                # push 명령어 뒤에 오는 모든 값을 하나의 문자열로 합침
                value_to_push = " ".join(user_input[1:])
                stack.push(value_to_push)
            else:
                print("❌ Error: 'push' 명령어는 값이 필요합니다. (예: push hello)")

        elif command == "pop":
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"👍 Popped: '{popped_value}'")

        elif command == "peek":
            peeked_value = stack.peek()
            if peeked_value is not None:
                print(f"👀 Peeked: '{peeked_value}'")

        elif command == "size":
            print(f"📏 Size: {stack.size()}")

        elif command == "is_empty":
            if stack.is_empty():
                print("✅ The stack is empty.")
            else:
                print("❎ The stack is not empty.")

        elif command == "view":
            print(stack)

        elif command == "exit":
            print("👋 프로그램을 종료합니다.")
            break

        else:
            print(f"❓ '{command}'는 알 수 없는 명령어입니다. 다시 시도해주세요.")

if __name__ == "__main__":
    main()
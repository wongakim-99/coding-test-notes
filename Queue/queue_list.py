class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)  # rear에 삽입

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # front 에서 제거
        else:
            return "Queue is empty"  
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # front 에 있는 데이터 확인
        else:
            return "Queue is empty"
        
# 사용예시
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.peek())
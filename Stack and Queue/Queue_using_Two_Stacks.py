class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return -1

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        return -1

    def is_empty(self):
        return len(self.items) == 0


class QueueUsingStack:
    def __init__(self):
        self.S1 = Stack()
        self.S2 = Stack()

    def enqueue(self, value):
        self.S1.push(value)

    def dequeue(self):
        if self.S2.is_empty():
            while not self.S1.is_empty():
                self.S2.push(self.S1.pop())
        return self.S2.pop()

    def front(self):
        if self.S2.is_empty():
            while not self.S1.is_empty():
                self.S2.push(self.S1.pop())
        return self.S2.top()

queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
print(queue.front())   
print(queue.dequeue()) 

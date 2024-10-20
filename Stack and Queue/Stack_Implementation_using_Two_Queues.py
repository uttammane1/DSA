class Queue:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return -1
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return -1
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


class StackUsingQueue:
    def __init__(self):
        self.Q1 = Queue()
        self.Q2 = Queue()

    def push(self, value):
        self.Q1.push(value)

    def pop(self):
        if self.Q1.is_empty():
            return -1

        while len(self.Q1.items) > 1:
            self.Q2.push(self.Q1.pop())

        popped_value = self.Q1.pop()
        self.Q1, self.Q2 = self.Q2, self.Q1

        return popped_value

    def top(self):
        if self.Q1.is_empty():
            return -1

        while len(self.Q1.items) > 1:
            self.Q2.push(self.Q1.pop())

        top_value = self.Q1.front()
        self.Q2.push(self.Q1.pop())
        self.Q1, self.Q2 = self.Q2, self.Q1

        return top_value

stack = StackUsingQueue()
stack.push(10)
stack.push(20)
print(stack.top())  
print(stack.pop())  
print(stack.pop())  

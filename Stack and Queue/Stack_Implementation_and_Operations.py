class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)  # Add to the end of the list

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # Remove the last element
        else:
            return -1

    def top(self):
        if not self.is_empty():
            return self.items[-1]  # Get the last element
        else:
            return -1

    def is_empty(self):
        return len(self.items) == 0  # Check if stack is empty

stack = Stack()
stack.push(5)
stack.push(10)
print(stack.top())  
print(stack.pop())  

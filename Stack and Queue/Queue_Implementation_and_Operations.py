class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)  # Add to the end of the list

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove from the front
        else:
            return -1

    def front(self):
        if not self.is_empty():
            return self.items[0]  # Get the first element
        else:
            return -1

    def is_empty(self):
        return len(self.items) == 0  # Check if queue is empty

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
print(queue.dequeue())  
print(queue.front())    

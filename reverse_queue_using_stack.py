class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is Empty")
        else:
            return self.queue.pop(0)

    def display(self):
        print(self.queue)



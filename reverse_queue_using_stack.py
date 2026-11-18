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



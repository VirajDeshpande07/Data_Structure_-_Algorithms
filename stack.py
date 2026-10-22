class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty!")
            return None

        temp = self.top
        self.top = self.top.next
        return temp.data

    def print(self):
        if self.isempty():
            print("Stack is empty!")
            return

        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


st = Stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

print("Stack elements:")
st.print()

print("Popped element:", st.pop())

print("Stack after pop:")
st.print()
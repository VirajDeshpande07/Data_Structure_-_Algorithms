class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, pos=None):
        new_node = Node(data)

        if pos is None or pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data, pos=None):
        new_node = Node(data)

        if pos is None or pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    class LinkedList:
     def __init__(self):
        self.head = None

     def insert(self, data, pos=None):
        new_node = Node(data)

        if pos is None or pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(pos - 2):
            if temp is None:
                return
            temp = temp.next

        if temp is None:
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    
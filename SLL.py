class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def count(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count


list = LinkedList()

list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

list.print()
print("Count:", list.count())
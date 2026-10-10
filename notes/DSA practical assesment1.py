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

   

print("After deleting node at position 2:")
list.delete(2)
list.display()

print("Reversed linked list:")
list.reverse()
list.display()

print("Sum of consecutive nodes:")
list.consecutive_sums()

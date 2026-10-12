
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Delete middle node
    def delete_middle(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

    # Delete first node
    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next

    # Delete last node
    def delete_last(self):
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None


# Create linked list
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original linked list:")
ll.display()

# Delete middle node
ll.delete_middle()
print("\\nAfter deleting middle node:")
ll.display()

# Delete first node
ll.delete_first()
print("\\nAfter deleting first node:")
ll.display()

# Delete last node
ll.delete_last()
print("\\nAfter deleting last node:")
ll.display()

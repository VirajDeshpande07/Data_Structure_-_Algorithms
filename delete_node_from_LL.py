class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Delete node by value
    def delete(self, value):
        if self.head is None:
            print("List is empty")
            return

        # Delete first node
        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted")
                return

            temp = temp.next

        print("Value not found")

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original list:")
ll.display()

# Delete node
ll.delete(30)

print("After deletion:")
ll.display()

# Reverse list
ll.reverse()

print("After reversing:")
ll.display()
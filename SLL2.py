# Singly Linear Linked List

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at the end
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Insert node at a particular position
    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            p = 1
            temp = self.head

            while p != pos - 1:
                temp = temp.next
                p += 1

            new_node.next = temp.next
            temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Count number of elements
    def count(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        return count


# Creating linked list
list = LinkedList()

# Appending elements
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))

print("Original Linked List:")
list.display()

print("Number of elements:", list.count())

# Insert 15 at position 2
list.insert(Node(15), 2)

print("\nAfter inserting 15 at position 2:")
list.display()

print("Number of elements:", list.count())
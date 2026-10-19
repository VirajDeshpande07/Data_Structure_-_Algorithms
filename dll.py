
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def count_occ(self,num):
        temp=self.head
        count=0
        while temp:
            if temp.data==num:
                count+=1
            temp=temp.next
        return count

    def Insert(self, new_node, position):
        if position == 0:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    def print(self):
        temp = self.head
        print("List elements:")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def delete(self, value):
        temp = self.head

        while temp and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value is not present in the list")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Deleted:", value)


list1 = LinkedList()
list1.append(Node(22))
list1.append(Node(33))
list1.append(Node(44))
list1.append(Node(55))

list1.Insert(Node(5), 0)

list1.print()
list1.delete(5)
list1.print()
print("Occurrences of 33:", list1.count_occ(33))
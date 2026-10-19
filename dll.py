class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

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

    def print(self):
        temp = self.head
        print("List elements:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

 #delete a node from the doubly linked list
    def delete(self, value):
        temp = self.head
        if temp.data == value: #first node to delete
            self.head=self.head.next
            self.head.prev=None
        else:
            while(temp.data!=value and temp):
                temp=temp.next
                if temp==None:
                    print("value is not present in the list")
                    return
            temp.prev.next=temp.next
            temp=None
    


list1 = LinkedList()
list1.append(Node(22))
list1.append(Node(33))
list1.append(Node(44))
list1.append(Node(55))

list1.print()
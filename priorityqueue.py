class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Add Patient (Enqueue)
    def enqueue(self, new_node):

        if self.front is None:
            self.front = self.rear = new_node
            print("Patient added successfully")
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            print("Patient added successfully")
            return

        temp = self.front

        while temp.next is not None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.rear = new_node

        print("Patient added successfully")

    # 2. Display Next Patient
    def display_next(self):
        if self.front is None:
            print("Priority queue is empty")
            return

        print("\nNext Patient to be Treated:")
        print("Patient ID:", self.front.pid)
        print("Patient Name:", self.front.name)
        print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):
        if self.front is None:
            print("Priority queue is empty")
            return

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print("Patient treated and removed:", temp.name)


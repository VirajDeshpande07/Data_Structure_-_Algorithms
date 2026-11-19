class Node:
    def __init__(self,value):
        self.right=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self, new_node):
        if self.root is None:
            self.root=new_node
            return 


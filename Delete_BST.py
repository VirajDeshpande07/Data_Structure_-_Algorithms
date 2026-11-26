# BST using Linked List
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, new_node):
        if self.root is None:  ##BST is empty
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:  # left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:  # right subree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def delete(self, rt, value):
        if rt is None:
            return
        if value < rt.data:
            rt.left = self.delete(rt.left, value)
        elif value > rt.data:
            rt.right = self.delete(rt.right, value)
        else:
            if rt.left is None:  # Node with right child only
                return rt.right
            if rt.right is None:  # Node with left child only
                return rt.left
            # Node has both Left and right
            succ = self.get_sucessor(rt)
            rt.data = succ.data  # Fixed '-' to '='
            rt.right = self.delete(rt.right, succ.data)
        return rt

    
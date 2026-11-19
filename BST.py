
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:

                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)

    def preorder(self, temp):
        if temp is not None:
            print(temp.data, end=" ")
            self.preorder(temp.left)
            self.preorder(temp.right)

    def postorder(self, temp):
        if temp is not None:
            self.postorder(temp.left)
            self.postorder(temp.right)
            print(temp.data, end=" ")


# Main program
tree = BST()

tree.insert(Node(50))
tree.insert(Node(30))
tree.insert(Node(70))
tree.insert(Node(20))
tree.insert(Node(40))
tree.insert(Node(60))
tree.insert(Node(80))

print("Inorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


tree = BinaryTree()

tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.insert(2)
tree.insert(8)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(10)
tree.insert(9)

print("Preorder: ")
tree.preorder(tree.root)
print("\nInorder: ")
tree.inorder(tree.root)
print("\nPostorder: ")
tree.postorder(tree.root)



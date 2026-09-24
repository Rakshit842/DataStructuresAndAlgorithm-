class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(22)
root.left = Node(4)
root.right = Node(5)

root.left.left=Node(6)
root.left.right=Node(9)


# Inorder Traversal
# Left -> Root -> Right
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
print("Inorder Traversal:")
inorder(root)

# Preorder Traversal
# Root -> Left -> Right
def preorder(node):
    if node:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("Preorder Traversal:")
preorder(root)


# Postorder Traversal
# Left -> Right -> Root
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
print("Postorder Traversal:")
postorder(root)
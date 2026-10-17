
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

root = None
n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    root = insert(root, data)

print("Inorder Traversal:", end=" ")
inorder(root)

print("\nPreorder Traversal:", end=" ")
preorder(root)

print("\nPostorder Traversal:", end=" ")
postorder(root)
print()


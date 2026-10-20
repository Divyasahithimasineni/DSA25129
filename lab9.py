
# Binary Tree Operations and Traversals

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
    else:
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

def levelorder(root):
    if root is None:
        print("Tree is empty")
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = None

while True:
    print("\n\n1. Insert")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Level Order")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        value = int(input("Enter value: "))
        root = insert(root, value)
        print("Node inserted")

    elif ch == 2:
        print("Inorder:")
        inorder(root)

    elif ch == 3:
        print("Preorder:")
        preorder(root)

    elif ch == 4:
        print("Postorder:")
        postorder(root)

    elif ch == 5:
        print("Level Order:")
        levelorder(root)

    elif ch == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")

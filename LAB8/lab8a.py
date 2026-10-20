
# Week 8: Binary Tree using Array

tree = []

def insert(value):
    tree.append(value)
    print(value, "inserted successfully")

def display():
    if len(tree) == 0:
        print("Tree is empty")
    else:
        print("Binary Tree elements:", tree)

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        insert(value)

    elif choice == 2:
        display()

    elif choice == 3:
        break

    else:
        print("Invalid choice")

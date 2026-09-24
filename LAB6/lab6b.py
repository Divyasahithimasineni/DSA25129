# Stack implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self):
        element = int(input("Enter element to push: "))

        new_node = Node(element)
        new_node.next = self.top
        self.top = new_node

        print(element, "pushed into stack")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            element = self.top.data
            self.top = self.top.next
            print(element, "popped from stack")

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element is:", self.top.data)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements are:")

            while temp is not None:
                print(temp.data)
                temp = temp.next


# Menu-driven program
stack = Stack()

while True:
    print("\n--- STACK USING LINKED LIST ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")

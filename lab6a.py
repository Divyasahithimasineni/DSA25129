# Stack implementation using Array

stack = [32,45,34,435,324,45,543]
MAX_SIZE = 5


def push():
    if len(stack) == MAX_SIZE:
        print("Stack Overflow")
    else:
        element = int(input("Enter element to push: "))
        stack.append(element)
        print(element, "pushed into stack")


def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        element = stack.pop()
        print(element, "popped from stack")


def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element is:", stack[-1])


def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements are:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])


# Menu-driven program
while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")

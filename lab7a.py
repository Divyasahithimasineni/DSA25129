# Queue Implementation using Array
# Operations: Enqueue, Dequeue, Peek, Display

queue = []
MAX_SIZE = 5

while True:
    print("\n----- QUEUE USING ARRAY -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) == MAX_SIZE:
            print("Queue Overflow! Queue is full.")
        else:
            value = int(input("Enter element to enqueue: "))
            queue.append(value)
            print(value, "inserted into queue.")

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow! Queue is empty.")
        else:
            value = queue.pop(0)
            print(value, "deleted from queue.")

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Front element:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty.")
        else:
            print("Queue elements:", queue)

    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice! Please try again.")

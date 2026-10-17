
size = int(input("Enter the size of circular queue: "))
queue = [None] * size
front = -1
rear = -1

def enqueue():
    global front, rear

    if (rear + 1) % size == front:
        print("Queue Overflow")
    else:
        element = int(input("Enter element to insert: "))

        if front == -1:
            front = 0

        rear = (rear + 1) % size
        queue[rear] = element
        print("Element inserted successfully")

def dequeue():
    global front, rear

    if front == -1:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue[front])

        if front == rear:
            front = rear = -1
        else:
            front = (front + 1) % size

def display():
    if front == -1:
        print("Queue is empty")
    else:
        print("Queue elements:", end=" ")
        i = front

        while True:
            print(queue[i], end=" ")
            if i == rear:
                break
            i = (i + 1) % size

        print()

while True:
    print("\n--- Circular Queue Operations ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

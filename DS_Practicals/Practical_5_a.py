
queue = []
size = int(input("Enter the size of queue: "))

def enqueue():
    if len(queue) == size:
        print("Queue Overflow")
    else:
        element = int(input("Enter element to insert: "))
        queue.append(element)
        print("Element inserted successfully")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue.pop(0))

def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)

while True:
    print("\n--- Queue Operations ---")
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


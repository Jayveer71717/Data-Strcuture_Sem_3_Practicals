
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert_beginning():
    global head
    data = int(input("Enter data: "))
    new_node = Node(data)

    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        new_node.next = head
        temp.next = new_node
        head = new_node

    print("Node inserted at beginning")

def insert_end():
    global head
    data = int(input("Enter data: "))
    new_node = Node(data)

    if head is None:
        head = new_node
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        temp.next = new_node
        new_node.next = head

    print("Node inserted at end")

def insert_after():
    data = int(input("Enter node value after which to insert: "))
    value = int(input("Enter new data: "))

    if head is None:
        print("Linked list is empty")
        return

    temp = head

    while True:
        if temp.data == data:
            break
        temp = temp.next
        if temp == head:
            print("Given node not found")
            return

    new_node = Node(value)
    new_node.next = temp.next
    temp.next = new_node
    print("Node inserted successfully")

def display():
    if head is None:
        print("Linked list is empty")
        return

    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break

    print("(back to head)")

while True:
    print("\n--- Singly Circular Linked List ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert after a given node")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_beginning()
    elif choice == 2:
        insert_end()
    elif choice == 3:
        insert_after()
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert_beginning():
    global head
    data = int(input("Enter data: "))
    new_node = Node(data)
    new_node.next = head
    head = new_node
    print("Node inserted at beginning")

def insert_end():
    global head
    data = int(input("Enter data: "))
    new_node = Node(data)

    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    print("Node inserted at end")

def insert_after():
    global head
    key = int(input("Enter node value after which to insert: "))
    data = int(input("Enter new data: "))

    temp = head
    while temp is not None and temp.data != key:
        temp = temp.next

    if temp is None:
        print("Given node not found")
    else:
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted successfully")

def display():
    temp = head

    if temp is None:
        print("Linked list is empty")
        return

    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

while True:
    print("\n--- Singly Linked List ---")
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


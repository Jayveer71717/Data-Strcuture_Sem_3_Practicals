
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

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

def delete_first():
    global head

    if head is None:
        print("Linked list is empty")
    else:
        print("Deleted node:", head.data)
        head = head.next

def delete_last():
    global head

    if head is None:
        print("Linked list is empty")
    elif head.next is None:
        print("Deleted node:", head.data)
        head = None
    else:
        temp = head
        while temp.next.next is not None:
            temp = temp.next

        print("Deleted node:", temp.next.data)
        temp.next = None

def delete_after():
    key = int(input("Enter node value: "))
    temp = head

    while temp is not None and temp.data != key:
        temp = temp.next

    if temp is None:
        print("Given node not found")
    elif temp.next is None:
        print("No node exists after the given node")
    else:
        print("Deleted node:", temp.next.data)
        temp.next = temp.next.next

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
    print("1. Insert at end")
    print("2. Delete first node")
    print("3. Delete last node")
    print("4. Delete node after a given node")
    print("5. Display all nodes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_end()
    elif choice == 2:
        delete_first()
    elif choice == 3:
        delete_last()
    elif choice == 4:
        delete_after()
    elif choice == 5:
        display()
    elif choice == 6:
        break
    else:
        print("Invalid choice")


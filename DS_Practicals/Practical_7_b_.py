
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
        new_node.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next
        temp.next = new_node
        new_node.next = head

def delete_first():
    global head

    if head is None:
        print("List is empty")
        return

    if head.next == head:
        print("Deleted node:", head.data)
        head = None
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        print("Deleted node:", head.data)
        head = head.next
        temp.next = head

def delete_last():
    global head

    if head is None:
        print("List is empty")
        return

    if head.next == head:
        print("Deleted node:", head.data)
        head = None
    else:
        temp = head
        while temp.next.next != head:
            temp = temp.next

        print("Deleted node:", temp.next.data)
        temp.next = head

def delete_after():
    if head is None:
        print("List is empty")
        return

    key = int(input("Enter node value: "))
    temp = head

    while temp.data != key:
        temp = temp.next
        if temp == head:
            print("Given node not found")
            return

    if temp.next == temp:
        print("No node exists after the given node")
    else:
        deleted = temp.next
        print("Deleted node:", deleted.data)

        temp.next = deleted.next

        if deleted == head:
            global_head_update(temp)

def global_head_update(temp):
    global head
    head = temp.next

def display():
    if head is None:
        print("List is empty")
        return

    temp = head
    while True:
        print(temp.data, end=" -> ")
        temp = temp.next
        if temp == head:
            break
    print("(back to head)")

while True:
    print("\n--- Circular Linked List ---")
    print("1. Insert at end")
    print("2. Delete first node")
    print("3. Delete last node")
    print("4. Delete node after a given node")
    print("5. Display")
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

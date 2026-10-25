class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None


# 1. Insert at beginning
def insert_beginning():
    global head
    data = int(input("Enter data: "))
    new = Node(data)

    if head is None:
        head = new
        new.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        new.next = head
        temp.next = new
        head = new

    print("Node inserted")


# 2. Insert at end
def insert_end():
    global head
    data = int(input("Enter data: "))
    new = Node(data)

    if head is None:
        head = new
        new.next = head
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        temp.next = new
        new.next = head

    print("Node inserted")


# 3. Insert after given node
def insert_after():
    global head

    if head is None:
        print("List is empty")
        return

    key = int(input("Enter node value: "))
    data = int(input("Enter new data: "))
    temp = head

    while True:
        if temp.data == key:
            new = Node(data)
            new.next = temp.next
            temp.next = new
            print("Node inserted")
            return

        temp = temp.next
        if temp == head:
            break

    print("Node not found")


# 4. Delete first node
def delete_first():
    global head

    if head is None:
        print("List is empty")
        return

    if head.next == head:
        head = None
    else:
        temp = head
        while temp.next != head:
            temp = temp.next

        head = head.next
        temp.next = head

    print("First node deleted")


# 5. Delete last node
def delete_last():
    global head

    if head is None:
        print("List is empty")
        return

    if head.next == head:
        head = None
    else:
        temp = head
        while temp.next.next != head:
            temp = temp.next

        temp.next = head

    print("Last node deleted")


# 6. Delete node after given node
def delete_after():
    global head

    if head is None:
        print("List is empty")
        return

    key = int(input("Enter node value: "))
    temp = head

    while True:
        if temp.data == key:
            if temp.next == temp:
                head = None
            else:
                delete_node = temp.next
                temp.next = delete_node.next

                if delete_node == head:
                    head = temp.next

            print("Node deleted")
            return

        temp = temp.next
        if temp == head:
            break

    print("Node not found")


# 7. Display
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

    print("(HEAD)")


# Main menu
while True:
    print("\n--- Singly Circular Linked List ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert after given node")
    print("4. Delete first node")
    print("5. Delete last node")
    print("6. Delete after given node")
    print("7. Display")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        insert_beginning()
    elif choice == 2:
        insert_end()
    elif choice == 3:
        insert_after()
    elif choice == 4:
        delete_first()
    elif choice == 5:
        delete_last()
    elif choice == 6:
        delete_after()
    elif choice == 7:
        display()
    elif choice == 8:
        break
    else:
        print("Invalid choice")
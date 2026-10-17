
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert_end(data):
    global head
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

def display():
    if head is None:
        print("Linked list is empty")
        return

    temp = head
    print("Circular Linked List:", end=" ")

    while True:
        print(temp.data, end=" -> ")
        temp = temp.next

        if temp == head:
            break

    print("(back to head)")

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    insert_end(data)

display()

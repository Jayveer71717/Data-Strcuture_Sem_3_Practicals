
import array

# Function to create an array
def create_array():
    n = int(input("Enter size of array: "))
    arr = array.array('i')

    for i in range(n):
        element = int(input(f"Enter element {i + 1}: "))
        arr.append(element)

    return arr

# Function for insertion
def insertion(arr):
    pos = int(input("Enter position for insertion: "))
    element = int(input("Enter element to insert: "))

    arr.insert(pos - 1, element)
    print("Array after insertion:", arr)

# Function for deletion
def deletion(arr):
    element = int(input("Enter element to delete: "))

    if element in arr:
        arr.remove(element)
        print("Array after deletion:", arr)
    else:
        print("Element not found")

# Function for traversal
def traversal(arr):
    print("Array elements:")
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# Function for searching
def search(arr):
    element = int(input("Enter element to search: "))

    for i in range(len(arr)):
        if arr[i] == element:
            print("Element found at position", i + 1)
            return

    print("Element not found")

# Main program
arr = create_array()

print("Original array:", arr)

insertion(arr)
deletion(arr)
traversal(arr)
search(arr)

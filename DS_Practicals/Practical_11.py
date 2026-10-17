def binary_search(list1, key):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high) // 2

        if list1[mid] == key:
            print("Element found at index:", mid)
            return

        elif list1[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    print("Element not found")


list1 = [10, 20, 30, 40, 50, 60]
key = int(input("Enter element to search: "))

binary_search(list1, key)
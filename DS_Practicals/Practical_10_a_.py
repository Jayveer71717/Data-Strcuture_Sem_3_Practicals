def bubble_sort(list1):
    for i in range(len(list1)):
        for j in range(len(list1) - 1 - i):
            if list1[j] > list1[j + 1]:
                temp = list1[j]
                list1[j] = list1[j + 1]
                list1[j + 1] = temp

    print("Sorted list:", list1)


list1 = [5, 3, 8, 1, 2]
bubble_sort(list1)
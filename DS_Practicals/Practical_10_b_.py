def selection_sort(list1):
    for i in range(len(list1)):
        min_index = i

        for j in range(i + 1, len(list1)):
            if list1[j] < list1[min_index]:
                min_index = j

        temp = list1[i]
        list1[i] = list1[min_index]
        list1[min_index] = temp

    print("Sorted list:", list1)


list1 = [5, 3, 8, 1, 2]
selection_sort(list1)
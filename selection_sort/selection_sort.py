def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp

    return arr


my_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_list = selection_sort(my_list)
print("Sorted:", sorted_list)


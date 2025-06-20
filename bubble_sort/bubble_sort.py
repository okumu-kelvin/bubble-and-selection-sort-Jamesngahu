def bubble_sort(unsorted_list):
    for i in range(len(unsorted_list) - 1):
        for j in range(len(unsorted_list) - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:

                temp = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j + 1]
                unsorted_list[j + 1] = temp
    return unsorted_list

my_list = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_list = bubble_sort(my_list)
print("Sorted:", sorted_list)


def selection_sort(arr, size):
    for i in range(size - 1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index], arr[i]
    return arr


a = [4,2,6,5,1,3]
sorted_list = selection_sort(a, len(a))
print(sorted_list)



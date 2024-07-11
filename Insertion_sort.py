def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i - 1 
        while temp < arr[j] and j >=0:
            arr[j+1] = arr[j]
            arr[j] = temp
            j-=1 
    return arr




l = [23,12,45,33,2,17,5,89,14]
insertion_sort(l)
print('The sorted array is :\n',l)



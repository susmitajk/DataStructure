# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
    
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)
    
#     # Build a max heap
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
    
#     # Extract elements one by one
#     for i in range(n - 1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)

# arr = [4, 10, 3, 5, 1, 6, 0, 9]
# heap_sort(arr)
# print("Sorted array is:", arr)


def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

def heap_sort(arr):
    n = len(arr)
    
    # Build a min-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract the elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [4, 10, 3, 5, 1, 6, 0, 9]
heap_sort(arr)
print('The sorted array:', arr)




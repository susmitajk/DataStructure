class MinHeap:
    def __init__(self):
        self.heap = []
    
    #creating the helper function
    def _parent(self,index):
        return (index-1)//2
    
    def _left_child(self,index):
        return 2*index + 1
    
    def _right_child(self,index):
        return 2*index + 2
    
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    
    def insert(self,element):
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)
    
    def _heapify_up(self,index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index,parent_index)
            self._heapify_up(parent_index)
    
    def remove(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap)-1)
            root = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            root = self.heap.pop()
        else:
            root = None
        return root
    
    def _heapify_down(self,index):
        smallest = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self._swap(index,smallest)
            self._heapify_down(smallest)
    
    def build_heap(self,array):
        self.heap = array[:]
        for i in range(len(array)//2-1,-1,-1):
            self._heapify_down(i)
    
    def display(self):
        print('The Heap is :')
        print(self.heap)
        print('\n')



min1 = MinHeap()
min1.insert(12)
min1.insert(11)
min1.insert(13)
min1.insert(15)
min1.insert(6)
min1.insert(7)

min1.display()
print('\n')
print('\nThe largest element from the heap is:',min1.remove())
print('\nheap after deletion:')
min1.display()

min2 = MinHeap()
arr = [10,25,2,78,44,21,7,55]
min2.build_heap(arr)
print('\n-------the min2 heap is--------')
min2.display()
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    # creating healper functions
    def _parent(self,index):
        return (index-1)//2
    
    def _left_child(self, index):
        return 2*index+1 
    
    def _right_child(self, index):
        return 2*index+2
    
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    
    def insert(self,element):
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)
    
    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index,parent_index)
            self._heapify_up(parent_index)
    
    def remove(self):
        if len(self.heap) > 1:
            self._swap(0,len(self.heap)-1)
            root = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            root = self.heap.pop()
        else:
            root = None
        return root
    
    def _heapify_down(self, index):
        largest = index
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self._swap(index,largest)
            self._heapify_down(largest)
    
    def build_heap(self,array):
        self.heap = array[:]
        for i in range(len(array)//2-1,-1,-1):
            self._heapify_down(i)
    
    def display(self):
        print('The heap is:')
        print(self.heap, end = ' ')
        print('\n')
        
        
max1 = MaxHeap()
max1.insert(12)
max1.insert(11)
max1.insert(13)
max1.insert(15)
max1.insert(6)
max1.insert(7)

max1.display()
print('\n')
print('\nThe largest element from the heap is:',max1.remove())
print('\nheap after deletion:')
max1.display()

max2 = MaxHeap()
arr = [10,25,2,78,44,21,7,55]
max2.build_heap(arr)
print('\n-------the max2 heap is--------')
max2.display()

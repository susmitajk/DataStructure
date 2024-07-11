class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")
        return self.queue.pop(0)
        
    def peek(self):
        if self.isEmpty():
            print("The Queue is Empty")
        return self.queue[0]
    
    def change(self,index,item):
        if index < 0 or index >= len(self.queue):
            raise IndexError("The Given index is out of range")
        self.queue[index] = item
    
    def display(self):
        print("The queue elements are:")
        print(self.queue)

q1 = Queue()
q1.display()
print("##########################################")
for i in range(5):
    q1.enqueue(i)
q1.display()
q1.enqueue(5)
q1.display()
print('the current front element is:', q1.peek())
print("##########################################")
print("DEQUEUE:")
q1.dequeue()
q1.display()
print('the current front element is:', q1.peek())
print("##########################################")
q1.change(2,34)
q1.display()
print('the current front element is:', q1.peek())
print("##########################################")
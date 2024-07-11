class Stack:
    def __init__(self, max_size=None):
        self.stack = []
        self.max_size = max_size
    
    def isEmpty(self):
        return len(self.stack) == 0 
    
    def isFull(self):
        if self.max_size is None:
            return False
        return len(self.stack) >= self.max_size
    
    def push(self, item):
        if self.isFull():
            raise Exception("Stack Overflow")
        self.stack.append(item)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise Exception("Stack Underflow")
        
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            return self.stack[-1]  # returning the top element
    
    def count(self):
        return len(self.stack)
    
    def change(self, index, item):
        if index < 0 or index >= self.count():
            raise IndexError("Position Out of Range")
        self.stack[index] = item
    
    def display(self):
        print('The Stack Elements are:')
        print(self.stack)

        
stack1 = Stack(3)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.display()

# stack1.push(4)

stack1.pop()
stack1.display()  
        
stack1.pop()
stack1.display()  

stack1.pop()
stack1.display()  

# stack1.pop()
# stack1.display()  

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.display()

# Print the count of elements in the stack
print("Count:", stack1.count())

print("Peek:", stack1.peek())

stack1.change(1,7)
stack1.display()
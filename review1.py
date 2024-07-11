class stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def isFull(self):
        return len(self.stack) >= self.max_size
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        self.stack.pop()
    
    def palindrom(self):
        reverse_stack = self.stack[::-1]
        if self.stack == reverse_stack:
            return True 
        else:
            return False
    
    def display(self):
        print("The stack is:")
        print(self.stack)
        
s1 = stack(10)
s1.push('r')
s1.push('a')
s1.push('d')
s1.push('a')
s1.push('r')
s1.display()
print(s1.palindrom())

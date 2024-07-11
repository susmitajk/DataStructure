class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end =' <-> ')
            temp = temp.next
        print(None)
    
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def prepend(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length//2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self,index,data):
        temp = self.get(index) 
        if temp:
            temp.data = data
            return True
        return False
    
    def insert(self,index,data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        new_node = Node(data)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            temp.prev = after
            before = temp
            temp = after





my_double = DoublyLinkedList()
my_double.print_list()

#appending the first element
print('\n################################')
my_double.append(2)
print('\n list after append:')
my_double.print_list()
print('\n################################')
my_double.append(3)
print('\n list after append:')
my_double.print_list()
print('\n################################')
my_double.prepend(1)
print('\n list after prepand:')
my_double.print_list()
print('\n################################')
my_double.prepend(1)
print('\n list after prepend:')
my_double.print_list()
print('\n################################')
my_double.insert(2,2)
print('\n list after insert(2,2):')
my_double.print_list()
print('\n################################')
my_double.insert(2,3)
print('\n list after insert(2,2):')
my_double.print_list()
print('\n################################')
my_double.insert(1,12)
print('\n list after insert(2,2):')
my_double.print_list()
print('\n################################')
my_double.pop()
print('\n list after popping from tail:')
my_double.print_list()
print('\n################################')
my_double.pop_first()
print('\n list after popping from head:')
my_double.print_list()
print('\n################################')
my_double.remove(2)
print('\n list after removed from index:')
my_double.print_list()
print('\n################################')
my_double.remove(0)
print('\n list after removed from index:')
my_double.print_list()
print('\n################################')
my_double.reverse()
print('\n list revrsal:')
my_double.print_list()
print('\n################################')
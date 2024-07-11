class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end = ' -> ')
            temp = temp.next
        print('None')
        
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
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
            before = temp
            temp = after
    

    def delete_by_node_value(self, value):
        if self.length == 0:
            return False
        # Deleting the head:
        if self.head.value == value:
            return self.pop_first()
        
        pre = self.head
        temp = self.head.next
        while temp:
            if temp.value == value:
                pre.next = temp.next 
                temp.next = None
                self.length -= 1
                if temp == self.tail:  # if the node to be deleted is at the end
                    self.tail = pre
                    self.tail.next = None
                return True
            pre = temp
            temp = temp.next 
        return False      


    def insert_before_x(self, x, new_value):
        # if the x is found at the beginning
        if self.head.value == x:
            return self.prepend(new_value)
        
        new_node = Node(new_value)
        pre = self.head
        temp = self.head.next
        while temp:
            if temp.value == x:
                new_node.next = temp
                pre.next = new_node
                self.length += 1
                return True
            pre = temp
            temp = temp.next
        return False # value not found
    
    def insert_after_x(self, x, new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.value == x:
                new_node.next = temp.next
                temp.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.length += 1
                return True
            temp = temp.next
        return False  # Value not Found
    
    # remove duplicates from the  sorted linked list:
    def remove_duplicate(self):
        current = self.head
        while current and current.next:
            if current.value == current.next.value:
                current.next = current.next.next 
                self.length -= 1
            else:
                current = current.next
        return True
    

    



        
        
        




print('\n#################################')
my_linked_list = LinkedList(1) # creating first node
print('\n the linked list after first node creation:')
my_linked_list.print_list()
print('\n')
print('\n#################################')
my_linked_list.append(1) # adding node at the end
print('\n the linked list after second node creation:')
my_linked_list.print_list()
print('\n#################################')
my_linked_list.append(2)  # adding node at the end
print('\n the linked list after third node creation:')
my_linked_list.print_list()
# print('\n the linked list after prepand:')
# my_linked_list.print_list()
print('\n#################################')

my_linked_list.prepend(1) # addinig node at the beginning
print('\n the linked list after prepand:')
my_linked_list.print_list()

print('\n#################################')
my_linked_list.prepend(-1) # addinig node at the beginning
print('\n Linked list after prepand:')
my_linked_list.print_list()

print('\n#################################')
my_linked_list.insert(5, 2) # inserting node at specific position
print('\n Linked list after insertion:')
my_linked_list.print_list()

print('\n#################################')
my_linked_list.pop()
print('\n Linked list after pop:')
my_linked_list.print_list()

print('\n#################################')
my_linked_list.pop_first()
print('\n Linked list after popping first element:')
my_linked_list.print_list()
print('\n#################################')
my_linked_list.prepend(-1)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.print_list()
print('\n#################################')
my_linked_list.remove_duplicate()
print('\n linked list after removing duplicate')
my_linked_list.print_list()
# print('\n#################################')
# my_linked_list.reverse()
# print('\n Reversed linked list is:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.delete_by_node_value(25)
# print('\n Linked list after deleting by node value:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_before_x(20, 1)
# print('\n Linked List insert_before_x:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_before_x(30, 2)
# print('\n Linked List insert_before_x:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_before_x(10, 0)
# print('\n Linked List insert_before_x:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_after_x(0, 9)
# print('\n Linked List insert_after_x:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_after_x(2, 19)
# print('\n Linked List insert_after_x:')
# my_linked_list.print_list()

# print('\n#################################')
# my_linked_list.insert_after_x(1, 29)
# print('\n Linked List insert_after_x:')
# my_linked_list.print_list()

# print('\n#################################')


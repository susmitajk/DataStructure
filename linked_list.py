#creating a node of the liked list:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# Creating a class LinkedList() to facilitate ll operations
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    # to print the Linked List elements
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next  
        print(None)
    
    # to add a node to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        # empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    # to add a node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)
        # empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        return True
    
    # to delete a node at the end of the list
    def pop(self):
        # empty list 
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        # in case of single node in the list
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    # to delete a node from th ebeginnning of the list 
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # In casse of single element
        if self.length == 0:
            self.tail = None
        return temp
    
    # get a node at the specified index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # to update the value of a node at specified index
    def set_value(self,index,data):
        temp = self.get(index)
        if temp:
            temp.data = data
            return True
        return False
    
    # to insert a node at a specified index
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(data)
        if index == self.length:
            return self.append(data)
        new_node = Node(data)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True
    
    # to remove a node from the specified index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return  self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
    
    def insert_before_x(self,x,new_value):
        new_node = Node(new_value)
        # insertion at the begininig
        if self.head.data == x:
            return self.prepend(new_value)
        
        prev = self.head
        temp = self.head.next
        while temp:
            if temp.data == x:
                new_node.next = temp
                prev.next = new_node
                self.length += 1
                return True
            prev =  temp
            temp = temp.next
        return True
    
    def insert_after_x(self,x,new_value):
        new_node = Node(new_value)
        temp = self.head
        while temp:
            if temp.data == x:
                new_node.next = temp.next
                temp.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.length += 1
                return True
            temp = temp.next
        return False

    def remove_by_value(self, x):
        if self.length == 0:
            return False
        if self.head.data == x:
            return self.pop_first()
        prev = self.head
        temp = self.head.next
        
        while temp:
            if temp.data == x:
                prev.next = temp.next
                temp.next = None
                self.length -= 1
                if temp == self.tail:
                    self.tail= prev
                    self.tail.next = None
                return True
            prev = temp
            temp = temp.next 
        return False
    

    def merge_sorted_list(self,l1,l2):
        dummy = Node(0)
        tail = dummy

        current1 = l1.head
        current2 = l2.head

        while current1 and current2:
            if current1.data <= current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next 
        
        if current1:
            tail.next = current1
        else:
            tail.next = current2
        
        merged_list = LinkedList()
        merged_list.head = dummy.next

        #calculate the length of the merged list
        temp = merged_list.head
        while temp:
            merged_list.length += 1
            temp = temp.next
        
        merged_list.tail = tail

        return merged_list
    

        
        
        
            
             







            


    


        
    




# created an empty list
my_linked_list = LinkedList()    
# prints empty list
my_linked_list.print_list()
print('#########################################\n')
# adding first element into the list
my_linked_list.append(2)
my_linked_list.print_list()
print('#########################################\n')
# adding a node at the beginning 
my_linked_list.prepend(1)
my_linked_list.print_list()
print('#########################################\n')
# popping a node from the end
my_linked_list.pop()
my_linked_list.print_list()
print('#########################################\n')
my_linked_list.insert(1,2)
my_linked_list.print_list()
print('#########################################\n')
my_linked_list.insert_before_x(1,0)
my_linked_list.print_list()
print('#########################################\n')
my_linked_list.insert_after_x(2,3)
my_linked_list.print_list()
print('#########################################\n')
my_linked_list.insert_after_x(2,23)
my_linked_list.print_list()
print('#########################################\n')
my_linked_list.remove_by_value(23)
my_linked_list.print_list()
print('#########################################\n')


print("Merging two sorted list")
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.print_list()  # 1 -> 3 -> 5 -> None

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
list2.print_list()
print('\nmerged list:')
merge_list = list1.merge_sorted_list(list1,list2)
merge_list.print_list()
print('#########################################\n')
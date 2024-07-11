class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print(None)
    
    def is_palindrome(self):
        # Find the middle of the linked list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Compare the first and second halves
        left = self.head
        right = prev
        while right:  # Only need to compare till the end of the shorter half
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        
        return True

# Example usage:
ll = LinkedList()
arr = [1, 2, 3, 2, 1]
for item in arr:
    ll.append(item)

ll.print_list()  # 1 -> 2 -> 3 -> 2 -> 1 -> None
print(ll.is_palindrome())  # True

ll2 = LinkedList()
arr2 = [1, 2, 3, 4, 5]
for item in arr2:
    ll2.append(item)

ll2.print_list()  # 1 -> 2 -> 3 -> 4 -> 5 -> None
print(ll2.is_palindrome())  # False

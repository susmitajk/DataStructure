# implementing bst
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # inserting nodes into the tree 
    def insert(self,value):
        def insert_helper(node,value):
            if node is None:
                return Node(value)
            elif value < node.data:
                node.left = insert_helper(node.left, value)
            if value > node.data:
                node.right = insert_helper(node.right, value)
            return node
        self.root = insert_helper(self.root, value)
    
    # searching a node in the binary tree
    def contains(self,value):
        def contains_helper(node, value):
            if node is None:
                return False
            if value < node.data:
                return contains_helper(node.left, value)
            elif value > node.data:
                return contains_helper(node.right, value)
            else:
                return True
        return contains_helper(self.root, value)
        
    #deleing a specified node
    def delete(self, value):
        def delete_helper(node,value):
            if node is None:
                return node
            if value < node.data:
                node.left = delete_helper(node.left, value)
            elif value > node.right:
                node.right = delete_helper(node.right,value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.find_min_node(node.right)
                node.data = temp
                node.right = delete_helper(node.right, temp)
            return node
        self.root = delete_helper(self.root,value)
    
    def find_min_node(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data
    
    def find_max_node(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
    
    def in_order_traversal(self,node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end =' ')
            self.in_order_traversal(node.right)
            
    def pre_order_traversal(self,node):
        if node is not None:
            print(node.data, end= ' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    def post_order_traversal(self,node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.data, end= ' ')
    
    def height_of_tree(self,node):
        if node is None:
            return -1
        left_height = self.height_of_tree(node.left)
        right_height = self.height_of_tree(node.right)
        return max(left_height,right_height) + 1
    
    def depth_of_node(self,value):
        def depth_finder(node,value,depth):
            if node is None:
                return -1
            if value == node.data:
                return depth
            if value < node.data:
                return depth_finder(node.left, value, depth + 1)
            else:
                return depth_finder(node.right, value, depth + 1)
        return depth_finder(self.root, value, 0)
    
    def size(self):
        def size_helper(node):
            if node is None:
                return 0
            left_size = size_helper(node.left)
            right_size = size_helper(node.right)
            return left_size + right_size + 1
        
        return size_helper(self.root)
    
    def left_view(self):
        result = []
        queue = deque([self.root])
        if not self.root:
            return []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    def right_view(self):
        result = []
        queue = deque([self.root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size -1:
                    result.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

bst = BST()
list1 = [10,5,15,2,12,20,1,25,26]
for i in list1:
    bst.insert(i)

print('In-order-traversal:')
bst.in_order_traversal(bst.root)
print('\n*********************************\n')                   
print('\npre-order-traversal:')
bst.pre_order_traversal(bst.root)                    
print('\n*********************************\n')     
print('\nPost-order-traversal:')
bst.post_order_traversal(bst.root)  
print('\n*********************************\n')      
print('\nthe height of the tree is:', bst.height_of_tree(bst.root))
print('*********************************')    
print('\ndepth of the node 15 is :', bst.depth_of_node(15))
print('*********************************')    
print('\nLeft view of the tree is :', bst.left_view())      
print('*********************************')            
print('\nRight view of the tree is :', bst.right_view())     
print('*********************************')       
print('\nMax Node of the tree is :', bst.find_max_node()) 
print('*********************************')  
print('\nMin Node of the tree is :', bst.find_min_node(bst.root)) 
print('*********************************') 
print('\nNo.of Nodes in given the tree is :', bst.size()) 
print('*********************************')   
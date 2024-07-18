class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        def insert_helper(node,value):
            if node is None:
                return Node(value)  
            if value < node.data:
                node.left = insert_helper(node.left, value)
            elif value > node.data:
                node.right = insert_helper(node.right,value)
            return node # returning root node bub tree root node
                
        self.root = insert_helper(self.root,value)
    
    def closest_node(self, target):
        closest = float('inf')
        current = self.root
        while current is not None:
            if abs(target - closest) > abs(target - current.data):
                closest = current.data
            if target < current.data:
                current = current.left
            elif target > current.data:
                current = current.right
            else:
                break
        return closest
    
    def in_order_traversal(self,node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.data, end = ' ')
            self.in_order_traversal(node.right)
        
        
        
    
bst = BST()
list1 = [10,5,15,2,7,12,20]
for i in list1:
    bst.insert(i)

bst.in_order_traversal(bst.root)
print('\n')
print(bst.closest_node(12))
            
        
    
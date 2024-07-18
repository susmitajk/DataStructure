class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
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
        
    def is_BST(self):
        def in_order_traversal(node, result):
            if node is not None:
                in_order_traversal(node.left,result)
                result.append(node.data)
                in_order_traversal(node.right, result)
        
        result = []
        in_order_traversal(self.root,result)
        
        for i in range(1,len(result)):
            if result[i-1] > result[i]:
                return False
        return True
    

tree = BST()
tree.root = Node(10)
tree.root.left = Node(5)
tree.root.right = Node(15)
tree.root.left.left = Node(2)
# tree.root.left.right = Node(7)
tree.root.right.left = Node(12)
tree.root.right.right = Node(20)

print('\n')
print("Is the binary tree a BST (in-order method)?",tree.is_BST())
        
        
        
# Implementing Binary Tree
class BST:
    def __init__(self, key = None):
        self.key = key
        self.left = self.right = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return 
        if data == self.key:
            return 
        if data < self.key:
            if self.left:
                self.left.insert(data)    # recursive call to check the left sub tree
            else:
                self.left = BST(data)
                return
        else:
            if self.right:
                self.right.insert(data)    # recursive call to check the right sub tree
            else:
                self.right = BST(data)
                return
            
    def contains(self,data):
        if self.key == data:
            print('Node Found')
            return 
        if data < self.key:
            if self.left:
                self.left.contains(data)
            else:
                print('Node Not Found')
        else:
            if self.right:
                self.right.contains(data)
            else:
                print('Node Not Found')
    
    def pre_order_traversal(self):
        pass

    def in_order_traversal(self):
        pass

    def post_order_traversal(self):
        pass
    
    def delete(self,data):
        pass
            

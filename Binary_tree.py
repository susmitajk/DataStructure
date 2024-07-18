class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def insert_helper(node, value):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = insert_helper(node.left, value)
            elif value > node.value:
                node.right = insert_helper(node.right, value)
            return node
        self.root = insert_helper(self.root, value)

    def contains(self, value):
        def contains_helper(node, value):
            if node is None:
                return False
            if value < node.value:
                return contains_helper(node.left, value)
            elif value > node.value:
                return contains_helper(node.right, value)
            else:
                return True
        return contains_helper(self.root, value)

    def delete_node(self, value):
        def delete_helper(node, value):
            if node is None:
                return node
            if value < node.value:
                node.left = delete_helper(node.left, value)
            elif value > node.value:
                node.right = delete_helper(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self.find_min_node(node.right)
                node.value = temp.value
                node.right = delete_helper(node.right, temp.value)
            return node
                
        self.root = delete_helper(self.root, value)

    def find_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max_node(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node

    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value, end=' ')
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value, end=' ')
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value, end=' ')

# Test the BinarySearchTree class
bst = BinarySearchTree()
list1 = [20, 4, 30, 1, 5, 6]
for i in list1:
    bst.insert(i)

print("In-order traversal:")
bst.in_order_traversal(bst.root)
print('\n')

print("Pre-order traversal:")
bst.pre_order_traversal(bst.root)
print('\n')

print("Post-order traversal:")
bst.post_order_traversal(bst.root)
print('\n')

print("Contains 5:", bst.contains(5))
bst.delete_node(5)
print("Contains 5 after deletion:", bst.contains(5))
print('\nTree after deletion:')
bst.in_order_traversal(bst.root)
print('\n')



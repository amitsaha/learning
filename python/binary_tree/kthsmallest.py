'''
Implement an iterator on a binary search tree such that
it returns the smallest element every time it is called
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    
    inorder_nodes = []

    def __init__(self, value):
        self.root = Node(value)
        self.left = None
        self.right = None
    
    def insert(self, value, root=None):
        if not root:
            root = self.root        
        if value < root.value:
            if root.left:
                self.insert(value, root=root.left)
            else:
                root.left = Node(value)
        else:
            if root.right:
                self.insert(value, root=root.right)
            else:
                root.right = Node(value)

    def inorder(self, root=None):
        if not root:
            root = self.root
        if root.left:
            self.inorder(root=root.left)
        self.inorder_nodes.append(root.value)
        if root.right:
            self.inorder(root=root.right)
          
t = Tree(1)
t.insert(2)
t.insert(-1)
t.insert(5)
t.insert(3)
t.inorder()

# for the kth smallest, print the k+1 th element from
# this list
print t.inorder_nodes

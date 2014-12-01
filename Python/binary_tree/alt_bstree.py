class Node:
    
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self, root):
        self.root = root

    def insert(self, root, node):
                    
        if node.item < root.item:
            if not root.left:
                root.left = node
            else:
               self.insert(root.left, node)
        else:
            if not root.right:
                root.right = node
            else:
                self.insert(root.right, node)

    def visit(self, node):
        print(node.item)

    def inorder(self, root):
        if root.left:
            self.inorder(root.left)        
        self.visit(root)
        if root.right:
            self.inorder(root.right)

    def max_depth(self, root):
        # leaf node
        if not root:      
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))
        
           

t = BinaryTree(Node(10))
t.insert(t.root, Node(11))
t.insert(t.root, Node(2))
t.insert(t.root, Node(-1))
t.insert(t.root, Node(7))
t.insert(t.root, Node(17))
t.inorder(t.root)
print(t.max_depth(t.root))


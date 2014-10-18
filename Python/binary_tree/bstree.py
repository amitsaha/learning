"""
Binary search tree
"""
from collections import deque

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def children_count(self):

        count = 0

        if self.left:
            count += 1
        if self.right:
            count += 1

        return count

    def lookup(self, data, parent=None):

        if self.data == data:
            return self, parent
        if data < self.data:
            if self.left is None:
                return None
            else:
                return self.left.lookup(data, parent=self)
        else:
            if self.right is None:
                return None
            else:
                return self.right.lookup(data, parent=self)

    # aka bfs traversal
    def level_traversal(self):

        root = self
        dq = deque()
        dq.append(root)
        while dq:
            root = dq.popleft()
            if root.left:
                dq.append(root.left)
            if root.right:
                dq.append(root.right)
            print root.data

    def mirror_image(self):

        root = self
        dq = deque()
        dq.append(root)

        while dq:
            root = dq.popleft()
            if root.right:
                dq.append(root.right)
            if root.left:
                dq.append(root.left)
            print root.data

    def delete(self, data):
        node, parent = self.lookup(data)
        if node.children_count() == 0:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            del node
        elif node.children_count() == 1:
            if node.left:
                n = node.left
            else:
                n = node.right
            if parent:
                if parent.left == node:
                    parent.left = n
                else:
                    parent.right = n
            del node
        else:
            # find the successor
            parent = node
            successor = node.right
            while successor.left:
                parent = successor
                successor = successor.left

            node.data = successor.data
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right

    def inorder(self):

        if self.left:
            self.left.inorder()

        print self.data

        if self.right:
            self.right.inorder()

    def preorder(self):

        print self.data
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):

        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print self.data

    def dfs(self):
        
        stack = list()
        stack.append(self)

        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print node.data

    def height(self):
        if not self.left:
            return 0
        if not self.right:
            return 0
        if self.left:
            h1 = self.left.height()
        if self.right:
            h2 = self.left.height()
            
        return 1 + max([h1, h2])

    # O(n) space where n: number of nodes in the tree
    def if_balanced(self):

        queue = deque()
        queue.append(self)

        while queue:
            root = queue.pop()
            if root.left:
                h1 = root.left.height()
                queue.append(root.left)
            if root.right:
                h2 = root.right.height()
                queue.append(root.right)

            if abs(h1-h2) > 1:
                return -1
        
        return 1

    def find_min(self):
        
        if not self.left:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        
        if not self.right:
            return self.data
        else:
            return self.right.find_max()
        

root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

# look up
#print root.lookup(6)
# level traversal
#root.level_traversal()
#mirror image
#root.mirror_image()
#root.delete(3)
#root.level_traversal()


# inorder
#root.inorder()
# pre order
#root.preorder()
# postorder
#root.postorder()
# size
#root.size()
#root.dfs()
#print root.height()
#print root.if_balanced()


print root.find_min()
print root.find_max()

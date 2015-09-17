'''
Level order binary tree traversal
'''

from collections import deque

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(None)
n5 = Node(2)
n6 = Node(None)
n7 = Node(3)

'''
         1
       /   \
      2     2
     / \   /  \
    3  None   3
'''

# setup left tree
n1.left = n2
n2.left = n3
n2.right = n4

# setup right tree
n1.right = n5
n5.left = n6
n5.right = n7

nodes = deque([n1])
while nodes:
    current_node = nodes.popleft()
    print current_node.value
    if current_node.left:
        nodes.append(current_node.left)
    if current_node.right:
        nodes.append(current_node.right)       
        

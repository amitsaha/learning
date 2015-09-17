'''
Is a binary tree a  mirror
'''

from collections import deque

class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None       

# Example of mirror

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(None)
# n5 = Node(2)
# n6 = Node(None)
# n7 = Node(3)

# # setup left tree
# n1.left = n2
# n2.left = n3
# n2.right = n4

# # setup right tree
# n1.right = n5
# n5.left = n6
# n5.right = n7


# Example of mirror

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(2)
# n4 = Node(3)
# n5 = Node(4)
# n6 = Node(4)
# n7 = Node(3)

# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n3.left = n6
# n3.right = n7

# Example of non-mirror

n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4 = Node(None)
n5 = Node(3)
n6 = Node(None)
n7 = Node(3)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# check if the two trees are mirror of each other
# first level traverse the left subtree
nodes = deque([n1.left])
left_nodes = []
while nodes:
    current_node = nodes.popleft()
    left_nodes.append(current_node.value)
    if current_node.left:
        nodes.append(current_node.left)
    if current_node.right:
        nodes.append(current_node.right)
        
# first level traverse the left subtree
nodes = deque([n1.right])
right_nodes = []
while nodes:
    current_node = nodes.popleft()
    right_nodes.append(current_node.value)
    if current_node.left:
        nodes.append(current_node.left)
    if current_node.right:
        nodes.append(current_node.right)

if left_nodes[0] == right_nodes[0] and left_nodes[1:] == right_nodes[1:][::-1]:
    print 'Mirror'
else:
    print 'Not mirror'

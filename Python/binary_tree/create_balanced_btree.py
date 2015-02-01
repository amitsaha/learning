'''
Create a balanced binary search tree from a given sorted array
'''

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root.left:
        preorder(root.left)
    print root.value
    if root.right:
        preorder(root.right)

def create_tree(arr, start, end):
    if start > end:
        return 
    mid = int((start + end)/2.0)
    root_val = arr[mid]    
    root = Node(root_val)
    root.left = create_tree(arr, start, mid-1)
    root.right = create_tree(arr, mid+1, end)

    return root

root = create_tree([1, 2, 3], 0, 2)
preorder(root)

root = create_tree([1, 2, 3, 4], 0, 3)
preorder(root)

# Linked list implementation in Python

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def add_after(head, data):
        
        trav = head
        while trav.next:
            trav = trav.next
        
        node = Node(data)
        trav.next = node

    def traverse(head):
        
        trav = head
        while trav:
            print trav.data
            trav = trav.next

    def delete(head, data):
        
        trav = head
        while trav:
            
            
        
        
        
# head
head = Node(1)
# add a node
head.add_after(2)
# traverse
head.traverse()

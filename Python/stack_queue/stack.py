from __future__ import print_function

class Node:

    def __init__(self, item):
        self.item = item

# unbounded stack
class Stack:
    def __init__(self):
        self.nodes = []
        self.top = -1

    def push(self, node):
        self.nodes.append(node)
        self.top += 1

    def pop(self):
        # prevent underflow
        if self.top >= 0:
            popped = self.nodes[self.top]
            self.top -= 1
            return popped
        else:
            return 'Stack empty'
s = Stack()
s.push(Node(1))
s.push(Node(2))
s.push(Node(3))

print(s.nodes)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

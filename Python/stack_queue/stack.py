from __future__ import print_function

class Node:

    def __init__(self, item):
        self.item = item
        self.min = item

    def __str__(self):
        return str(self.item)

# unbounded stack
class Stack:
    def __init__(self):
        self.nodes = []
        self.top = -1

    def push(self, node):
        if self.top >= 0:
            if self.nodes[self.top].min < node.item:
                node.min = self.nodes[self.top].min
        self.nodes.append(node)
        self.top += 1

    def pop(self):
        # prevent underflow
        if self.top >= 0:
            popped = self.nodes.pop(self.top)
            self.top -= 1
            return popped
        else:
            return 'Stack empty'

    def min(self):
        if self.top >= 0:
            return self.nodes[self.top].min

s = Stack()
s.push(Node(1))
s.push(Node(2))
print('Stack: %s' % str([n.item for n in s.nodes]))
print('Minimum: %d' % s.min())
s.push(Node(3))
s.push(Node(-1))
print('Stack: %s' % str([n.item for n in s.nodes]))
print('Minimum: %d' % s.min())

s.pop()
print('Stack: %s' % str([n.item for n in s.nodes]))
print('Minimum: %d' % s.min())
s.pop()
print('Stack: %s' % str([n.item for n in s.nodes]))
print('Minimum: %d' % s.min())
s.pop()
print('Stack: %s' % str([n.item for n in s.nodes]))
print('Minimum: %d' % s.min())
s.pop()

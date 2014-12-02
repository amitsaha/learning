'''
Sort a stack
'''

from __future__ import print_function
class Stack:

    def __init__(self):
        self.nodes = []

    def push(self, item):
        self.nodes.append(item)

    def pop(self):
        if self.nodes:
            return self.nodes.pop()

    def sort(self):
        t = []
        while self.nodes:
            tmp = self.nodes.pop()
            while t and t[-1] > tmp:
                self.nodes.append(t.pop())
            t.append(tmp)
        return t

s = Stack()
s.push(5)
s.push(3)
s.push(15)
s.push(-5)
print(s.nodes)
t = s.sort()
print(t)

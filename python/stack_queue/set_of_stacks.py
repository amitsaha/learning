'''
Implement a set of stacks data structure: each stack has a maximum capacity.
If one stack exceeds maximum capacity, the next element should go to a new stack.
'''
from __future__ import print_function

class SetOfStacks:

    def __init__(self):
        self.max = 5
        self.stacks = []

    def push(self, item):
        if self.stacks and len(self.stacks[-1]) < self.max:
            self.stacks[-1].append(item)
        else:
            new_stack = [item]
            self.stacks.append(new_stack)

    def pop(self):
        if self.stacks:
            popped = self.stacks[-1].pop()
            if not self.stacks[-1]:
                self.stacks.pop()
            return popped
        else:
            return 'Stack Empty'

s = SetOfStacks()
for i in range(12):
    s.push(i)
print(s.stacks)

for i in range(12):
    print(s.pop())
print(s.stacks)


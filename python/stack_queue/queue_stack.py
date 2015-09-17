'''
Queue implemented using two stacks
'''
class Queue:

    def __init__(self):
        # insert stack
        self.stack1 = []
        # remove stack
        self.stack2 = []

    def insert(self, node):
        self.stack1.append(node)

    def remove(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)

print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())

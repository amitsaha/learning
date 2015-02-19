'''
A data structure which has O(1) insert, remove (FIFO) and mode
'''
from collections import defaultdict

class Mystruct:

    def __init__(self):
        self.queue = []
        self.mode = 0
        self.count_table = defaultdict(lambda: 0)

    def insert(self, item):
        self.queue.append(item)
        self.count_table[item] += 1
        for k, v in self.count_table.items():
            if v > self.count_table[self.mode]:
                self.mode = k

    def remove(self):
        item = self.queue.pop(0)
        self.count_table[item] -= 1
        for k, v in self.count_table.items():
            if v > self.count_table[self.mode]:
                self.mode = k

        return item

s = Mystruct()
s.insert(1)
s.insert(-11)
s.insert(1)
s.insert(3)
s.insert(3)
s.insert(3)
s.insert(1)
s.insert(2)
s.insert(2)

print(s.remove())
print('Mode: ', s.mode)
print(s.remove())
print(s.remove())
print(s.remove())
print(s.remove())
print('Mode: ', s.mode)

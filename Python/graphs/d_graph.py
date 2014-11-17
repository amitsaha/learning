'''
Implement a directed graph and perform basic graph operations

Example graph:

        A -> B -> D
        |    |
       \ /  \/
   F <- C    E
        |    |
       \/   \/
       G     H
'''
from __future__ import print_function
from collections import deque

class Node:
    def __init__(self, label, neighbors=[]):
        self.label = label
        self.neighbors = neighbors

    def __str__(self):
        return self.label

def visit(node):
    print(node)

# breadth first search
def bfs(origin):
    # visit the origin
    visit(origin)
    # visit the neighbors
    to_visit = deque(origin.neighbors)
    while to_visit:
        cur = to_visit.popleft()
        to_visit.extend(cur.neighbors)
        visit(cur)

# depth first search
def dfs(origin):
    # visit the origin
    visit(origin)
    # visit the neighbors
    to_visit = origin.neighbors
    while to_visit:
        cur = to_visit.pop()
        to_visit.extend(cur.neighbors)
        visit(cur)

if __name__ == '__main__':
    d = Node('D')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    c = Node('C', neighbors=[f, g])
    e = Node('E', neighbors=[h])
    b = Node('B', neighbors=[d, e])
    a = Node('A', neighbors=[b, c])

    bfs(a)
    dfs(a)

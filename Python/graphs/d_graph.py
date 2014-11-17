'''
Implement a directed graph and perform basic graph operations
'''
from __future__ import print_function
from collections import deque, OrderedDict

class Node:
    def __init__(self, label, neighbors=[]):
        self.label = label
        self.neighbors = neighbors

    def __str__(self):
        return self.label + '->' + str([n.label for n in self.neighbors])

    def update_neighbors(self, neighbors=[]):
        self.neighbors = neighbors

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
def dfs(origin, visitor_func):
    # visit the origin
    visitor_func(origin)
    # visit the neighbors
    to_visit = origin.neighbors
    while to_visit:
        cur = to_visit.pop()
        to_visit.extend(cur.neighbors)
        visitor_func(cur)

# detect if there is a cycle in the graph
visited = OrderedDict()
def visit_with_cycle_detection(node):
    print(node)
    if not visited.get(node, None):
        visited[node] = True
    else:
        print('Cycle detected: {0}'.format(str([n.label for n in visited.keys()])))
        raise SystemExit

if __name__ == '__main__':
    '''
    Example graph:

        A -> B -> D
        |    |
       \ /  \/
   F <- C    E
        |    |
       \/   \/
       G     H
    '''
    d = Node('D')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    c = Node('C', neighbors=[f, g])
    e = Node('E', neighbors=[h])
    b = Node('B', neighbors=[d, e])
    a = Node('A', neighbors=[b, c])

    bfs(a)
    dfs(a, visit)

    # Graph with a cycle
    '''
          A -> C -> B
          |<------- |
    '''

    a = Node('A')
    b = Node('B')
    c = Node('C')
    a.update_neighbors([c])
    c.update_neighbors([b])
    b.update_neighbors([a])
    dfs(a, visit_with_cycle_detection)   

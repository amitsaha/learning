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

# Topological sort on a non-empty Acyclic graph
def toposort():
    '''
    7 -> 11, 8
    5 -> 11
    3 -> 8, 10
    11 -> 2, 9, 10
    8 -> 9
    '''
    two = Node('2')
    three = Node('3')
    five = Node('5')
    seven = Node('7')
    eight = Node('8')
    nine = Node('9')
    ten = Node('10')
    eleven = Node('11')

    seven.update_neighbors([eleven, eight])
    five.update_neighbors([eleven])
    three.update_neighbors([eight, ten])
    eleven.update_neighbors([two, nine, ten])
    eight.update_neighbors([nine])

    vertices = [two, three, five, seven, eight, nine, ten, eleven]
    # create the set of vertices with no incoming edges
    # -> vertex which is not in the right side of any of the nodes
    def get_vertices_with_incoming_edges():
        neighbors = []
        for v in vertices:
            if v.neighbors:
                neighbors.extend(v.neighbors)
        return set(neighbors)

    sorted_v = []
    with_incoming_edges = get_vertices_with_incoming_edges()
    no_incoming_edges = [v for v in vertices if v not in with_incoming_edges]
    while no_incoming_edges:
        n = no_incoming_edges.pop()
        sorted_v.append(n)
        for m in list(n.neighbors):
            # remove the edge from n to m
            n.neighbors.remove(m)
            with_incoming_edges = get_vertices_with_incoming_edges()
            if m not in with_incoming_edges:
                no_incoming_edges.append(m)

    if get_vertices_with_incoming_edges():
        print('Error')
    else:
        print([v.label for v in sorted_v])

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

    #bfs(a)
    #dfs(a, visit)

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
    #dfs(a, visit_with_cycle_detection)

    toposort()

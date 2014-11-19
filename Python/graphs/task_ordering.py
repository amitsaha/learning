'''
Find the task ordering from a set of dependency rules:

Example rules:

    3 -> 1 5
    2 -> 5 3
    4 -> 3
    5 -> 1

'''
from __future__ import print_function

class Node:
    def __init__(self, label, neighbors=[]):
        self.label = label
        self.neighbors = neighbors

    def __str__(self):
        return self.label + '->' + str([n.label for n in self.neighbors])

    def update_neighbors(self, neighbors=[]):
        self.neighbors = neighbors

def toposort():
    one = Node('1')
    two = Node('2')
    three = Node('3')
    four = Node('4')
    five = Node('5')

    # We create the graph in such a way that the dependencies
    # have vertices pointing towards the dependents and then just
    # do a topological sorting using Kahn's method
    one.update_neighbors([five])
    five.update_neighbors([two, three])
    three.update_neighbors([two, four])

    vertices = [one, two, three, four, five]
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
    toposort()

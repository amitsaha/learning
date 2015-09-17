'''
Searching a maze for a path from the entrance to the exit

S -> Start
E -> Exit

0 1 1 1 1 1  E
0 0 1 1 1 0
1 1 0 0 0 1
1 0 0 0 0 0

S
'''

def find_path(maze, s, e):
    


maze = [[0, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 0],
        [1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0]]

s = (3, 0)
e = (0, 5)
find_path(maze, s, e)

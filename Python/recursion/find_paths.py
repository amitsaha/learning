'''
Find a path for a robot to move from the left hand corner of a MxN grid
to the right hand corner
'''

M = 5
N = 5
current_path = []

def is_free(x, y):
    if x >= 0 and x < M and y >= 0 and y < N:
        return True
    else:
        return False

def find_path(x, y):
    # reached goal
    if x == M-1 and y == N-1:
        current_path.append((x, y))
        return current_path
    else:
        # Move right
        if is_free(x, y+1):
            current_path.append((x, y+1))
            find_path(x, y+1)
        # Move down
        if is_free(x+1, y):
            current_path.append((x+1, y))
            find_path(x+1, y)

find_path(0, 0)
print(current_path)

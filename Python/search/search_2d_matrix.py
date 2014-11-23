'''
Search for an element in a 2-D sorted matrix:

1 3 5
7 9 11
13 15 17
'''
from __future__ import print_function
def find_elem_matrix(mat, item):
    start = 0
    end = len(mat[0]) * len(mat) - 1

    while start <= end:
        mid = int((start+end)/2)
        r = int(mid % len(mat[0]))
        c = int(mid / len(mat[0]))

        if mat[r][c] == item:
            return r, c
        else:
            if mat[r][c] > item:
                end = mid - 1
            else:
                start = mid + 1

    return False

m = [[1, 3, 5],
     [7, 9, 11],
     [13, 15, 17]]
print(find_elem_matrix(m, 7))
print(find_elem_matrix(m, 9))
print(find_elem_matrix(m, 17))
print(find_elem_matrix(m, 90))

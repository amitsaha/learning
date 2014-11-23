'''
Search for an element in a 2-D  matrix
'''

from __future__ import print_function
'''
Sorted matrix:

1 3 5
7 9 11
13 15 17

'''

def find_elem_sorted_matrix(mat, item):
    start = 0
    end = len(mat[0]) * len(mat) - 1
    while start <= end:
        mid = int((start + end)/2)
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

print('Search in fully sorted matrix:')

print(find_elem_sorted_matrix(m, 7))
print(find_elem_sorted_matrix(m, 9))
print(find_elem_sorted_matrix(m, 18))


'''
Row sorted and column sorted:

1 2 8 9
2 4 9 12
4 7 10 13
6 8 11 15
'''
def find_elem_partially_sorted(mat, item):
    for row in range(len(mat)):
        start = 0
        end = len(mat[0]) - 1

        while start <= end:
            mid = int((start + end)/2)
            if mat[row][mid] == item:
                return row, mid
            else:
                if mat[row][mid] > item:
                    end = mid - 1
                else:
                    start = mid + 1
    return False

m = [[1, 2, 8, 9],
     [2, 4, 9, 12],
     [4, 7, 10, 13],
     [6, 8, 11, 15],]

print('Search in partially sorted matrix:')
print(find_elem_partially_sorted(m, 7))
print(find_elem_partially_sorted(m, 11))
print(find_elem_partially_sorted(m, 16))

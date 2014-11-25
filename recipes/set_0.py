'''
If an element in an MxN matrix is 0, set the entire row and column
to 0
'''

def setZero(mat):
    m = len(mat)
    n = len(mat[0])
    zero_rows = []
    zero_cols = []
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0 and i not in zero_rows and j not in zero_cols:
                mat[i] = [0]*n
                for k in range(m):
                    mat[k][j] = 0
                zero_rows.append(i)
                zero_cols.append(j)

    return mat

mat = [[1, 2, 0],
       [0, 5, 6],
       [3, 6, 7]]
mat = setZero(mat)

for i in range(len(mat)):
    print(mat[i][:])

print()
mat = [[1, 2, 1],
       [0, 5, 6],
       [3, 6, 7]]
mat = setZero(mat)
for i in range(len(mat)):
    print(mat[i][:])

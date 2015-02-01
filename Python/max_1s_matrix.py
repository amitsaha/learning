'''
Given a 2D matrix of 0s and 1s where each row contains the
0s and 1s in sorted order, find the row with the maximum number
of 1s
'''

def find_row_max_1s(mat):
    
    r = len(mat)
    c = len(mat[0])
    
    max_1s = 0
    row_num = 0

    for i in range(r):
        num1s = 0
        for j in range(c):
            if mat[i][j] == 1:
                num1s += c-j
                break
        # early exit
        if num1s == c:
            return i+1
        if num1s > max_1s:
            max_1s = num1s
            row_num = i

    return row_num+1

print(find_row_max_1s([[0, 0, 0, 1],
                       [1, 1, 1, 1 ],
                       [0, 0, 1, 1], 
                       [0, 1, 1, 1]]))

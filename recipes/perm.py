'''
Print all possible permutations for a given array

Can be used to print permutations of strings, sets, etc.
'''
from __future__ import print_function

def perm(arr, i):
    n = len(arr)
    if (i == n):
        print('Perm:' + str(arr))
    else:
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            perm(arr, i+1)
            arr[j], arr[i] = arr[i], arr[j]

perm([1, 2, 3], 0)

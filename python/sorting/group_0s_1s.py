'''
Groups the 0s and 1s together from a random array
Reference: http://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/
'''

from __future__ import print_function

def rearrange(arr):

    p1 = 0
    p2 = len(arr) - 1

    while p1 < p2:
        if arr[p1] == 0:
            p1 += 1
        if arr[p2] == 1:
            p2 -= 1
        if p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]

    return arr

print(rearrange([0, 0, 1, 1]))
print(rearrange([1, 0, 0, 1, 1]))
print(rearrange([1, 0, 0, 0, 1, 0, 0]))
print(rearrange([0, 1, 0, 1, 0, 1, 0, 1]))

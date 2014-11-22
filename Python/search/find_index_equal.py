'''
Find a number in a sorted array which is equal to its index value
'''
from __future__ import print_function

def find_index_element(arr, l, u):

    while l <= u:
        mid = int((l+u)/2)
        if (arr[mid] - mid == 0):
            return arr[mid], mid
        else:
            if (arr[mid] - mid) > 0:
                u = mid - 1
            else:
                l = mid + 1

    return False

arr = [-1, 1, 2, 4, 5, 6]
print(find_index_element(arr, 0, len(arr)-1))

arr = [-1, 0, 1, 2, 3, 4, 5, 7]
print(find_index_element(arr, 0, len(arr)-1))

arr = [0, 1, 2, 3, 4, 5, 8]
print(find_index_element(arr, 0, len(arr)-1))

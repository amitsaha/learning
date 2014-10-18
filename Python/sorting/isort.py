"""
Insertion sort

Features:

- In place
- Stable
- O(n^2)
- O(n) in the best case
- Constant extra space
"""
def isort(arr):
    for i in range(len(arr)):
        j = i
        while j>0 and arr[j] < arr[j-1]:
            # swap
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

arr = [-1, 100, 400, 90]
print isort(arr)
arr = [-1, 100, 400, 909]
print isort(arr)

"""
Quick sort

- Not in place

"""


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop(len(arr)/2)
    lesser, greater = [], []
    for item in arr:
        if item < pivot:
            lesser.append(item)
        else:
            greater.append(item)
    
    return qsort(lesser)+[pivot]+qsort(greater)

arr = [-1, 100, 400, 90]
print qsort(arr)
arr = [-1, 100, 400, 909]
print qsort(arr)


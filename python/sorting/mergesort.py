def merge(arr1, arr2):
    arr = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            arr.append(arr1[p1])
            p1 += 1
        else:
            arr.append(arr2[p2])
            p2 += 1
    if p1 < len(arr1):
        arr.extend(arr1[p1:])
    if p2 < len(arr2):
        arr.extend(arr2[p2:])
    
    return arr
        
def merge_sort(arr, l, u):

    if len(arr) <= 1:
        return arr
    boundary = len(arr)/2
    arr1 = arr[:boundary]
    arr2 = arr[boundary::]
    arr1 = merge_sort(arr1, 0, len(arr1))
    arr2 = merge_sort(arr2, 0, len(arr2))

    return merge(arr1, arr2)

a = [-10, 1, -7, 10, 5]
assert merge_sort(a, 0, len(a)) == [-10, -7, 1, 5, 10]
a = [0,-10, 1, -7, 10, 5, 3, 1000]
assert merge_sort(a, 0, len(a)) == [-10, -7, 0, 1, 3, 5, 10, 1000

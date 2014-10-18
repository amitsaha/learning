def merge(arr1, arr2):
    
    p1 = 0
    p2 = 0
    merged = []
    
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1

    if p1 == len(arr1):
        merged.extend(arr2[p2:])

    if p2 == len(arr2):
        merged.extend(arr1[p1:])

    return merged


def merge2():
    arr1 = [1,5,6]
    arr2 = [2,7,11]
    print merge(arr1, arr2)

def mergeN():
    arr1 = [1,5,6]
    arr2 = [2,7,11]
    arr3 = [3,8,17]

    arr = [arr1, arr2, arr3]

    merged = []

    for i in range(len(arr)):
        merged = merge(merged, arr[i])
    
    print merged

merge2()
mergeN()
    

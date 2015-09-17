'''
Find the k-th smallest element in a union of two given sorted arrays,
a and b
'''

# O(k) implementation
def findkth(a, b, k):
    
    i = 0
    j = 0
    found = 1
    while  i < len(a) and j< len(b):
        if a[i] < b[j]:
            smaller = a[i]
            i += 1
        else:
            smaller = b[j]
            j += 1
        kth_smallest = smaller
        if found == k:
            return kth_smallest
        else:
            found += 1
    
    if i < len(a):
        for num in a[i:]:
            kth_smallest = num
            if found == k:
                return kth_smallest
            else:
                found += 1
    if j < len(b):
        for num in b[j:]:
            kth_smallest = num
            if found == k:
                return kth_smallest
            else:
                found += 1
                
assert findkth([1, 2, 4], [3, 7, 11], 3) == 3
assert findkth([1, 2, 4, 5], [3, 7, 11], 5) == 5
assert findkth([1, 2], [3, 7, 11], 4) == 7
assert findkth([1, 2], [3, 7, 11], 5) == 11
assert findkth([1, 2], [-1, 7, 11], 1) == -1


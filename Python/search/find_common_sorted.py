"""
Find the common elements among two sorted sets

Desired time complexity: O(m+n)
"""

# Uses a hash table (hence uses O(min(m,n)) extra storage
# space
# This doesn't need the arrays to be sorted
def find_common(hash_t, arr):
    for item in arr:
        if hash_t.has_key(item):
            print item            

def find_sorted_hash(arr1, arr2):
    if len(arr1) < len(arr2):
        hash_t = {k:1 for k in arr1}
        find_common(hash_t, arr2)
    else:
        hash_t = {k:1 for k in arr2}
        find_common(hash_t, arr1)

# No extra storage space
# The array must be sorted
# O(m+n)
def find_common_traverse(arr1, arr2):
    
    i,j = 0,0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            print arr1[i]
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            i += 1

arr1 = [1,10,20,25,30]
arr2 = [1,10,30]

#find_sorted_hash(arr1, arr2)
find_common_traverse(arr1, arr2)

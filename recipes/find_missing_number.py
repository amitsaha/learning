'''
Find missing number between two arrays
'''

def find_missing(arr1, arr2):
    result = 0
    for item in arr1+arr2:
        result ^= item
    return result

print find_missing([1, 2, 3], [1, 2])
print find_missing([1, 2, 3], [1, 2, 10, 3])

'''
Find the least positive missing element from a sequence of positive
integers in 1..N
'''

def find_missing(arr):
    N = len(arr)

    # empty array
    if N == 0:
        return None

    # create a set to allow average O(1) lookup
    table = set(arr)
    for num in range(1, N+1):
        if num not in table:
            return num
    return None

# test cases
assert find_missing([]) == None
assert find_missing([1]) == None
assert find_missing([3, 4, 2, 2]) == 1
assert find_missing([3, 3, 1, 3]) == 2
assert find_missing([4, 4, 1, 3, 5]) == 2
assert find_missing([1, 1, 1, 1, 1]) == 2


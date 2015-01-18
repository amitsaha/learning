'''
Find the least positive missing element from a sequence of positive
integers in 1..N
'''

def find_missing(arr):
    N = len(arr)
    table = set(arr)

    if N == 1:
        if arr[0] != 1:
            return 1
        else:
            0
    for num in range(1, N+1):
        if num not in table:
            return num

assert find_missing([2]) == 1
assert find_missing([5, 4, 1, 3]) == 2
assert find_missing([6, 4, 1, 3, 5]) == 2

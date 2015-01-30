'''
Given an unsorted array of integers where all numbers appear
exactly even number of tiems. except for one. Find this integer.
'''

def oddmanout(arr):

    # O(n) space
    s = set()
    sum = 0
    # O(n)
    for num in arr:
        # O(1) lookup
        if num not in s:
            s.add(num)
        else:
            s.discard(num)
    assert len(s) == 1
    return [item for item in s][0]

assert oddmanout([1, 2, 2, 5, 5, 3, 3]) == 1
assert oddmanout([1, 2, 2, 5, 5, 3, 3, 1, 2, 2, 5, 5, 7, 7, 1]) == 1

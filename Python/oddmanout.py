'''
Given an unsorted array of integers where all numbers appear
exactly twice, except for one. Find this integer.
'''

def oddmanout(arr):

    # O(n) space
    s = set()
    sum = 0
    # O(n)
    for num in arr:
        # O(1) lookup
        if num not in s:
            sum += num
            s.add(num)
        else:
            sum -= num
    return sum

assert oddmanout([1, 2, 2, 5, 5, 3, 3]) == 1
assert oddmanout([1, 2, 2, 5, 5, 3, 3]) == 1

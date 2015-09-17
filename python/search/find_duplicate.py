'''
An array contains n numbers between 0 - n-2 with only one number duplicated.
Find the duplicated number
'''

def find_dup_1(arr, n):
    # find the sum of elements from 0..n-2
    sum1 = sum(range(0, n-1))
    # find the sum of the current elements
    sum2 = sum(arr)
    return sum2 - sum1

print(find_dup_1([0, 2, 1, 3, 2], 5))

'''
An array contains n numbers ranging from 0 to n-1. There are some
numbers duplicated in the array. Find the duplicated numbers
'''
def find_dup_2(arr):
    # O(n) but with additional space
    # use a set instead of dict to save the space
    # for the values
    d = set()
    for item in arr:
        if item in d:
            print(item)
        else:
            d.add(item)

find_dup_2([2, 1, 3, 2, 0, 5, 3])

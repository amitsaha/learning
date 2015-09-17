"""
Find numbers from three arrays which sum to a third
number
"""

import itertools

# Time: O(n^3)
# Space: O(1)
def find_tuple_1(a, b, c, k):
    
    # O(n^2)
    ab = itertools.product(a,b)
    # O(n^3)
    for p in ab:
        for n in c:
            if p[0] + p[1] + n == k:
                print p[0], p[1], n, k


# Time: O(n^2)
# Space: O(n)
def find_tuple_2(a, b, c, k):
    
    # O(n^2)
    ab = itertools.product(a,b)
    # O(n) space + time
    table = {n:1 for n in c}

    # O(n^2)
    for n in ab:
        # O(1)
        m = table.get(k-sum(n), None)
        if m:
            print n[0], n[1], k-sum(n), k

a = [1,2,3,4]
b = [5,6,7,8]
c = [10,12,13,14]
#find_tuple_1(a, b, c, 0)
#find_tuple_2(a, b, c, 0)

# find subsets of size three which sum to 0
d = [-1, 1, 0, 10, -10]
find_tuple_2(d, d, d, 0)

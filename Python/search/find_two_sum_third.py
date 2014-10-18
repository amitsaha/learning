"""
Find two numbers that sum to a third
"""

# uses O(n) extra storage
# O(n) time complexity
def approach1(numbers, k):

    # setup a dictionary with keys as the 
    # numbers and dummy values
    # O(n) + O(n)
    d = {k:1 for k in numbers}
    # O(n)
    for n in numbers:
        m = d.get(k-n, None)
        if m:
            return n,k-n
    
    return None

numbers = [1,3,10, 4]

# O(n)
for n in numbers:
    print n, approach1(numbers, n)

# print approach1([1,3,10], 13)
# print approach1([1,3,10,100], 101)
    

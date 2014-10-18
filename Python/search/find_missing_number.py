""""
Find the missing number from a sequence of 
numbers

"""

def find_missing(arr):
    n = len(arr)+1
    s = n*(n+1.0)/2.0
    return s - sum(arr)

print find_missing([5,4,2,1])
print find_missing([10,9,2,1, 8, 7, 6, 5, 4])

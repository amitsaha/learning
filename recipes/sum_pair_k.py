"""
Find the pairs of numbers that add to k
"""
def sum(arr, k):
    diff_dict = {item:k-item for item in arr}
    
    for k, v in diff_dict.iteritems():
        if diff_dict.get(v, False):
            print k, diff_dict[k]

sum([1, 2, 3, 4, 1], 7)

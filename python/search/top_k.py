'''
Find the top k frequent items in a stream of numbers 
'''
from collections import defaultdict, Counter
import heapq

# Approach 1: create a frequency table and then use
# heapq.nlargest with the key as the frequency for
# finding the k most frequently occuring items
def find_top_k_1(arr, k):
    count = defaultdict(lambda: 0)
    for item in arr:
        count[item] += 1
    return heapq.nlargest(k, count.keys(), lambda key:count[key])

# Approach 2: Create a Counter object and use the most_common()
# method
def find_top_k_2(arr, k):    
    return [item[0] for item in Counter(arr).most_common(k)]

print find_top_k_1([1, 
                    5, 
                    11, 
                    1, 
                    10, 
                    9, 
                    8, 
                    9], 
                   2)
print find_top_k_2([1, 
                    5, 
                    11, 
                    1, 
                    10, 
                    9, 
                    8, 
                    9], 2)

    

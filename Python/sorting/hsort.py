"""
Possibly O(nlogn) heap sort
"""

import heapq

def hsort(arr):

    # O(n)
    heapq.heapify(arr)
    
    while arr:
        print heapq.heappop(arr)

arr = [-1, 100, 400, 90]
hsort(arr)
arr = [-1, 100, 400, 909]
hsort(arr)


'''
Find the kth smallest element in an unsorted array
'''
import heapq
def kth_smallest(arr, k):

    # O(n) complexity
    heapq.heapify(arr)

    # k*log(n)
    for _ in range(k-1):
        # log(n)
        heapq.heappop(arr)
    return heapq.heappop(arr)


assert kth_smallest([5, 4, 3, 1, 10], 1) == 1
assert kth_smallest([5, 4, 3, 1, 10], 2) == 3
assert kth_smallest([5, 4, 3, 1, 10], 3) == 4

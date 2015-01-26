'''
Find the median element in an unsorted array
'''
import heapq
def find_median(arr):
    # O(n)
    heapq.heapify(arr)

    num_elements = len(arr)
    if num_elements % 2 != 0:
        return arr[(num_elements + 1)/2 - 1]
    else:
        return (arr[num_elements/2 - 1] + arr[num_elements/2 + 1 - 1])/2.0

assert find_median([1, -1, 2, 3, 4]) == 2
assert find_median([1, -1, 2, 3, 4, 5]) == 2.5

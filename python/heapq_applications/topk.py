import heapq

# initialize a heap
myheap = []
heapq.heapify(myheap)

def get_data(item):
    heapq.heappush(myheap, item)

get_data(2)
get_data(-1)
get_data(-100)
print myheap

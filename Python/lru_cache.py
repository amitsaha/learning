'''
Basic implementation of a LRU cache

- The main memory is implemented as a linear list
- The operation here is to search for the existence of an element in a list
- We cache the look up in a hash table (Python dictionary) which is of
  fixed size (max_size). If we find that the table is full, we evict the least
  recently used items.
- To implement the LRU scheme, we store the last accesses timestamp as the value
  of the key. If the table is filled, we evict the item with the earliest timestamp
'''

import time
import random
main_memory = [1, 10, 5, 'abc', -1]
lru_cache = {}
max_size = 3

def evict_lru():
    # remove the least recently used item from the cache
    min_timestamp = min([ts for item, ts in lru_cache.iteritems()])
    for item, ts in lru_cache.copy().iteritems():
        if ts == min_timestamp:
            print 'Evicting'
            lru_cache.pop(item)

def lookup(item):
    if item not in lru_cache:
        if len(lru_cache) >= max_size:
            evict_lru()
        # Linear look up
        if item in main_memory:
            lru_cache[item] = time.time()
        else:
            # just for fun
            print 'Going to disk'
    else:
        lru_cache[item] = time.time()

# test
for i in range(155):
    to_lookup = random.choice(main_memory)
    lookup(to_lookup)
    print to_lookup, lru_cache.keys()

'''
Sort an array of strings so that the anagrams 
are next to one another

Ex.

'abba', 'foo', 'bar', 'aabb'

becomes:

'abba', 'aabb', 'foo', 'bar'

'''
from __future__ import print_function
from collections import OrderedDict

def collect_anagrams(str_arr):
    d = OrderedDict()
    for i, s in enumerate(str_arr):
        t = ''.join(sorted(s))
        if not d.get(t, None):
            d[t] = [i]
        else:
            d[t].append(i)
    # at this stage, the dictionary, d has the sorted
    # strings as the keys and their positions as the values
    # so we just iterate over it and recreate a list
    str_arr_sorted = []
    for pos in d.values():
        for p in pos:
            str_arr_sorted.append(str_arr[p])
    return str_arr_sorted

print(collect_anagrams(['abba', 'foo', 'bar', 'aabb']))
print(collect_anagrams(['foo', 'bar', 'abba', 'rab',
                        'aabb']))
print(collect_anagrams(['foo', 'bar', 'abba', 'rab',
                        'aabb', 'oof']))
print(collect_anagrams(['I', 'yum', 'can', 'eat', 'I', 'ate', 'att', 'I', 'the', 'eel', 'eth', 'het']))

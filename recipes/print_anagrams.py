'''
Print all the anagrams in a list of words
'''

from __future__ import print_function

wordlist = ['abba',
            'baba',
            'caret',
            'cater']

# Using a lookup table
def approach1():
    d = {}
    # O(n)
    for w in wordlist:
        # O(klogk)
        w_s = ''.join(sorted(w))
        if d.get(w_s, None):
            d[w_s].append(w)
        else:
            d[w_s] = [w]
    for k, v in d.items():
        if v:
            print(v)

approach1()

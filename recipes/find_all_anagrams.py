'''
Find all anagrams in a list for a given lookup word 
(can be a file)
'''
from __future__ import print_function

wordlist = ['abba',
            'baba',
            'caret',
            'cater']

# Using a lookup table
def approach1(lookup):
    d = {}
    # O(n)
    for w in wordlist:
        # O(klogk)
        w_s = ''.join(sorted(w))
        if d.get(w_s, None):
            d[w_s].append(w)
        else:
            d[w_s] = [w]
    anagrams = d.get(''.join(sorted(lookup)))
    if anagrams:
        print(anagrams)

# sort the word and just read through the list of words
def approach2(lookup):
    # O(klogk)
    lookup_sorted = ''.join(sorted(lookup))
    for w in wordlist:
        # O(n)
        w_s = ''.join(sorted(w))
        if lookup_sorted == w_s:
            print(w)

# using primes
# Primes are multiplicatively unique
# So if we assign a prime number to each character, and find
# the product: anagrams will have the same product.
# This will prevent sorting

approach1('terac')
approach2('terac')

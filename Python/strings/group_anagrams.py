""" 
Anagram detection
"""

from collections import defaultdict

words = ['star', 'astr', 'car', 'rac', 'st']

anagrams = defaultdict(list)

for w in words:
    anagrams[''.join(sorted(w))].append(w)

print anagrams

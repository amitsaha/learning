'''
Find the first non-repeating character in a stream of
characters
'''

from collections import OrderedDict

def find_non_repeating(stream):
    
    table = OrderedDict()
    for c in stream:
        print 'Reading: ', c
        if c in table:
            table.pop(c)
        else:
            table[c] = 1
        print 'First non repeating character', table.keys()[0]

find_non_repeating('gefgiefk')
find_non_repeating('adbabc')
